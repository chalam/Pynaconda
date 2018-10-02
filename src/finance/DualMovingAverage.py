class DualMovingAverage(zp.TradingAlgorithm):
    def initialize(context):
        # we need to track two moving averages, so we will set
        # these up in the context the .add_transform method
        # informs Zipline to execute a transform on every day
        # of trading

        # the following will set up a MovingAverge transform,
        # named short_mavg, accessing the .price field of the
        # data, and a length of 100 days
        context.add_transform(zp.transforms.MovingAverage,
                              'short_mavg', ['price'],
                              window_length=100)

        # and the following is a 400 day MovingAverage
        context.add_transform(zp.transforms.MovingAverage,
                              'long_mavg', ['price'],
                              window_length=400)

        # this is a flag we will use to track the state of
        # whether or not we have made our first trade when the
        # means cross.  We use it to identify the single event
        # and to prevent further action until the next cross
        context.invested = False

    def handle_data(self, data):
        # access the results of the transforms
        short_mavg = data['AAPL'].short_mavg['price']
        long_mavg = data['AAPL'].long_mavg['price']

        # these flags will record if we decided to buy or sell
        buy = False
        sell = False

        # check if we have crossed
        if short_mavg > long_mavg and not self.invested:
            # short moved across the long, trending up
            # buy up to 100 shares
            self.order_target('AAPL', 100)
            # this will prevent further investment until
            # the next cross
            self.invested = True
            buy = True  # records that we did a buy
        elif short_mavg < long_mavg and self.invested:
            # short move across the long, trending down
            # sell it all!
            self.order_target('AAPL', -100)
            # prevents further sales until the next cross
            self.invested = False
            sell = True  # and note that we did sell

        # add extra data to the results of the simulation to
        # give the short and long ma on the interval, and if
        # we decided to buy or sell
        self.record(short_mavg=short_mavg,
                    long_mavg=long_mavg,
                    buy=buy,
                    sell=sell)

sub_data = data['1990':'2002-01-01']
sub_data.plot();
results = DualMovingAverage().run(sub_data)


def analyze(data, perf):
    fig = plt.figure()
    ax1 = fig.add_subplot(211, ylabel='Price in $')
    data['AAPL'].plot(ax=ax1, color='r', lw=2.)
    perf[['short_mavg', 'long_mavg']].plot(ax=ax1, lw=2.)

    ax1.plot(perf.ix[perf.buy].index, perf.short_mavg[perf.buy],
             '^', markersize=10, color='m')
    ax1.plot(perf.ix[perf.sell].index, perf.short_mavg[perf.sell],
             'v', markersize=10, color='k')

    ax2 = fig.add_subplot(212, ylabel='Portfolio value in $')
    perf.portfolio_value.plot(ax=ax2, lw=2.)

    ax2.plot(perf.ix[perf.buy].index,
             perf.portfolio_value[perf.buy],
             '^', markersize=10, color='m')
    ax2.plot(perf.ix[perf.sell].index,
             perf.portfolio_value[perf.sell],
             'v', markersize=10, color='k')

    plt.legend(loc=0)
    plt.gcf().set_size_inches(14, 10)

analyze(sub_data, results)

