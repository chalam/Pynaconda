data = zpf.load_from_yahoo(stocks=['PEP', 'KO'],
                              indexes={},
                              start=datetime(1997, 1, 1),
                              end=datetime(1998, 6, 1),
                              adjusted=True)
data.plot(figsize=(12,8));

# We will examine how the spread between the two stocks change
data['PriceDelta'] = data.PEP - data.KO
data['1997':].PriceDelta.plot(figsize=(12, 8))
plt.ylabel('Spread')
plt.axhline(data.Spread.mean());

# Using this information, we can make a decision to buy one stock and sell the other if the spread exceeds a particular size. In the algorithm we implement, we will normalize the spread data on a 100-day window and use that to calculate the z-score on each particular day.
#
# If the z-score is > 2, then we will want to buy PEP and sell KO as the spread increases over our threshold with PEP taking the higher price. If the z-score is < -2, then we want to buy KO and sell PEP, as PEP takes the lower price as the spread increases. Additionally, if the absolute value of the z-score < 0.5, then we will sell off any holdings we have in either stock to limit our exposure as we consider the spread to be fairly stable and we can divest.
#
# One calculation that we will need to perform during the simulation is calculating the regression of the two series prices. This will then be used to calculate the z-score of the spread at each interval. To do this, the following function is created:


@zp.transforms.batch_transform
def ols_transform(data, ticker1, ticker2):
    p0 = data.price[ticker1]
    p1 = sm.add_constant(data.price[ticker2], prepend=True)
    slope, intercept = sm.OLS(p0, p1).fit().params
    return slope, intercept


class Pairtrade(zp.TradingAlgorithm):
    def initialize(self, window_length=100):
        self.spreads = []
        self.invested = False
        self.window_length = window_length
        self.ols_transform = \
            ols_transform(refresh_period=self.window_length,
                          window_length=self.window_length)

    def handle_data(self, data):
        # calculate the regression, will be None until 100 samples
        params = self.ols_transform.handle_data(data, 'PEP', 'KO')
        if params:
            intercept, slope = params
            zscore = self.compute_zscore(data, slope, intercept)
            self.record(zscore=zscore)
            self.place_orders(data, zscore)

    def compute_zscore(self, data, slope, intercept):
        # calculate the spread
        spread = (data['PEP'].price - (slope * data['KO'].price +
                                       intercept))
        self.spreads.append(spread)  # record for z-score calc
        self.record(spread=spread)

        spread_wind = self.spreads[-self.window_length:]
        zscore = (spread - np.mean(spread_wind)) / np.std(spread_wind)
        return zscore

    def place_orders(self, data, zscore):
        if zscore >= 2.0 and not self.invested:
            # buy the spread, buying PEP and selling KO
            self.order('PEP', int(100 / data['PEP'].price))
            self.order('KO', -int(100 / data['KO'].price))
            self.invested = True
            self.record(action="PK")
        elif zscore <= -2.0 and not self.invested:
            # buy the spread, buying KO and selling PEP
            self.order('PEP', -int(100 / data['PEP'].price))
            self.order('KO', int(100 / data['KO'].price))
            self.invested = True
            self.record(action='KP')
        elif abs(zscore) < .5 and self.invested:
            # minimize exposure
            ko_amount = self.portfolio.positions['KO'].amount
            self.order('KO', -1 * ko_amount)
            pep_amount = self.portfolio.positions['PEP'].amount
            self.order('PEP', -1 * pep_amount)
            self.invested = False
            self.record(action='DE')
        else:
            # take no action
            self.record(action='noop')


perf = Pairtrade().run(data['1997':])
selection = ((perf.action=='PK') | (perf.action=='KP') |
                (perf.action=='DE'))
actions = perf[selection][['action']]
actions

ax1 = plt.subplot(411)
data[['PEP', 'KO']].plot(ax=ax1)
plt.ylabel('Price')

data.Spread.plot(ax=ax2)
plt.ylabel('Spread')

ax3 = plt.subplot(413)
perf['1997':].zscore.plot()
ax3.axhline(2, color='k')
ax3.axhline(-2, color='k')
plt.ylabel('Z-score')

ax4 = plt.subplot(414)
perf['1997':].portfolio_value.plot()
plt.ylabel('Protfolio Value')

for ax in [ax1, ax2, ax3, ax4]:
   for d in actions.index[actions.action=='PK']:
       ax.axvline(d, color='g')
   for d in actions.index[actions.action=='KP']:
       ax.axvline(d, color='c')
   for d in actions.index[actions.action=='DE']:
       ax.axvline(d, color='r')

plt.gcf().set_size_inches(16, 12)