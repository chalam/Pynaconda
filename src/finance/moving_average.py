from datetime import datetime

from pandas_datareader import data as pdr

msft = pdr.DataReader("MSFT", "google",
                      datetime(2017, 1, 1),
                      datetime.now())
print(msft[:5])

msft['MA7'] = pd.rolling_mean(msft['Adj Close'], 7)
msft['MA30'] = pd.rolling_mean(msft['Adj Close'], 30)
msft['MA90'] = pd.rolling_mean(msft['Adj Close'], 90)
msft['MA120'] = pd.rolling_mean(msft['Adj Close'], 120)

# Then, we plot the price versus various rolling means to see this concept of support:
msft['2014'][['Adj Close', 'MAm7',
              'MA30', 'MA120']].plot(figsize=(12, 8));

msft['2014'][['Adj Close', 'MA7',
              'MA30', 'MA120']].plot(figsize=(12, 8));


# Expo MA

periods = 10
alpha = 2.0/(periods +1)
factors = (1-alpha) ** np.arange(1, 11)
sum_factors = factors.sum()
weights = factors/sum_factors
weights
span = 90
msft_ewma = msft[['Adj Close']].copy()
msft_ewma['MA90'] = pd.rolling_mean(msft_ewma, span)
msft_ewma['EWMA90'] = pd.ewma(msft_ewma['Adj Close'],
                              span=span)
msft_ewma['2014'].plot(figsize=(12, 8));

# The exponential moving averages exhibit less lag, and, therefore, are more sensitive to recent prices and price changes. Since more recent values are favored, they will turn before simple moving averages, facilitating decision making on changes in momentum.
#
# Comparatively, a simple moving average represents a truer average of prices for the entire time period. Therefore, a simple moving average may be better suited to identify the support or resistance level.