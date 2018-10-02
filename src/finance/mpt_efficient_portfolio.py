# Mastering Pandas for Finance - Michael Heydt

import pandas as pd
import numpy as np
from pylab import plt, mpl
plt.style.use('seaborn')
mpl.rcParams['font.family'] = 'serif'

# The following command will create a DataFrame representing a portfolio:
def create_portfolio(tickers, weights=None):
    if (weights is None):
        shares = np.ones(len(tickers)) / len(tickers)
    portfolio = pd.DataFrame({'Tickers': tickers,
                              'Weights': weights},
                             index=tickers)
    return portfolio

portfolio = create_portfolio(['Stock A', 'Stock B'],
                            [1, 1])
print(portfolio)

returns = pd.DataFrame(
    {'Stock A': [0.1, 0.24, 0.05, -0.02, 0.2],
     'Stock B': [-0.15, -0.2, -0.01, 0.04, -0.15]})

print(returns)

# We can now calculate the equally-weighted portfolio and concatenate it with our original DataFrame of returns:
def calculate_weighted_portfolio_value(portfolio,
                                       returns,
                                       name='Value'):
    total_weights = portfolio.Weights.sum()
    weighted_returns = returns * (portfolio.Weights /
                                  total_weights)
    return pd.DataFrame({name: weighted_returns.sum(axis=1)})

wr = calculate_weighted_portfolio_value(portfolio,
                                       returns,
                                       "Value")
with_value = pd.concat([returns, wr], axis=1)
print(with_value)

# We can examine the volatility of each of the individual instruments combined with the results of the weighted portfolio, as shown here:
print(with_value.std())

# Stock A had a volatility of 11 percent and Stock B of 10 percent. The combined portfolio represented significantly lower volatility of 2 percent. This is because we picked two negatively correlated stocks with similar volatility and combining them has therefore reduced the overall risk.
# We can visualize this using the following function:
def plot_portfolio_returns(returns, title=None):
    returns.plot(figsize=(12, 8))
    plt.xlabel('Year')
    plt.ylabel('Returns')
    if (title is not None): plt.title(title)
    plt.show()

# plot_portfolio_returns()

# Just to check, we can also calculate the correlation of the original returns:
print(returns.corr())
# The returns of our two stocks have a negative correlation of -0.93, which tells us that they can be used to offset each other's volatility.


def get_historical_closes(ticker, start_date, end_date):
    p = web.DataReader(ticker, "yahoo", start_date, end_date)
    d = p.to_frame()['Adj Close'].reset_index()
    d.rename(columns={'minor': 'Ticker',
                      'Adj Close': 'Close'}, inplace=True)
    pivoted = d.pivot(index='Date', columns='Ticker')
    pivoted.columns = pivoted.columns.droplevel(0)
    return pivoted

closes = get_historical_closes(['MSFT', 'AAPL', 'KO'],
                                 '2010-01-01', '2014-12-31')

# Using this data, the following function will calculate annualized returns for each of the stocks. We start with the following function, which converts daily prices into daily returns:

def calc_daily_returns(closes):
    return np.log(closes / closes.shift(1))

daily_returns = calc_daily_returns(closes)
daily_returns[:5]

# From the daily returns, we can calculate annualized returns using the following function:

def calc_annual_returns(daily_returns):
   grouped = np.exp(daily_returns.groupby(
       lambda date: date.year).sum())-1
   return grouped

# This gives us the following as the annual returns:
annual_returns = calc_annual_returns(daily_returns)
annual_returns

# Formulation of portfolio risks
# Since we now have a return matrix, we can estimate its variance-covariance matrix, and by combining it with a vector of weights for each of the assets, we can calculate the overall portfolio variance (this flows into the Sharpe ratio calculation we will do next).

# The formulation of the portfolio variance starts with the calculation of the mean of the returns for an individual stock:
# Using this, we can then calculate the variance in the returns of a single stock:
# The return volatility is simply the square root of the variance:

# This can be very succinctly implemented in Python using NumPy arrays and matrices and the np.cov() function, which will calculate the covariance of the returns:
def calc_portfolio_var(returns, weights=None):
    if (weights is None):
        weights = np.ones(returns.columns.size) / \
                  returns.columns.size
    sigma = np.cov(returns.T, ddof=0)
    var = (weights * sigma * weights.T).sum()
    return var

# Using this function, the variance of our portfolio (using equal weighting for each stock) is determined by the following command:
calc_portfolio_var(annual_returns)

# The Sharpe ratio is a measurement of the risk-adjusted performance of portfolios. It is calculated by subtracting the risk-free rate from the expected return of a portfolio and then by dividing that result by the standard deviation of the portfolio returns.
def sharpe_ratio(returns, weights = None, risk_free_rate = 0.015):
   n = returns.columns.size
   if weights is None: weights = np.ones(n)/n
   var = calc_portfolio_var(returns, weights)
   means = returns.mean()
   return (means.dot(weights) - risk_free_rate)/np.sqrt(var)

sharpe_ratio(returns)

# Now that we can calculate the Sharpe ratio for a portfolio with a given set of weights,
# we need to be able to simulate the generation of different combinations of weights and
# select the weights where the Sharpe ratio is maximized. This will give us the efficient
#  portfolio. This simulation of weights will be performed using SciPy's optimization capabilities.
# We now need to perform optimizations to find the efficient portfolio. Optimizations
# in Python can be performed using scipy.optimize. We will first demonstrate optimization
# using a basic example and then later, we will optimize portfolios based on Sharpe ratios.
#
# Our basic example will be to minimize the following objective function:
# y = 2 + x^2
# Intuitively, we know that when x is 0, y is minimized. We can use this to check the
#  results of the minimization. The first step is to define the function we wish to minimize:

def y_f(x): return 2 + x ** 2

from scipy import optimize as scopt
scopt.fmin(y_f, 1000)
#    Optimization terminated successfully.
#             Current function value: 2.000000
#             Iterations: 27
#             Function evaluations: 54

# We are now able to create a function to use fmin() to determine the set of weights
# that maximize the Sharpe ratio for a given set of returns representing the stocks in
#  our portfolio.
#
# Since fmin() finds a minimum of the applied function, and the efficient portfolio exists
#  at the maximized Sharpe ratio, we need to provide a function that, in essence, returns
# the negative of the Sharpe ratio, hence allowing fmin() to find a minimum:
def negative_sharpe_ratio_n_minus_1_stock(weights,
                                          returns,
                                          risk_free_rate):
    """
    Given n-1 weights, return a negative sharpe ratio
    """
    weights2 = np.append(weights, 1 - np.sum(weights))
    return -sharpe_ratio(returns, weights2, risk_free_rate)

# Our final function is given a DataFrame of returns, and a risk-free rate will run a minimization process on our negative sharpe function. The process is seeded with an array of equal weights, and fmin() will start from those values and try different combinations of weights until we find the minimized negative Sharpe ratio. The function then returns a tuple of the weights satisfying the minimization, along with the optimal Sharpe ratio:
def optimize_portfolio(returns, risk_free_rate):
   w0 = np.ones(returns.columns.size-1,
                dtype=float) * 1.0 / returns.columns.size
   w1 = scopt.fmin(negative_sharpe_ratio_n_minus_1_stock,
                   w0, args=(returns, risk_free_rate))
   final_w = np.append(w1, 1 - np.sum(w1))
   final_sharpe = sharpe_ratio(returns, final_w, risk_free_rate)
   return (final_w, final_sharpe)

# Using this function, we can now determine the most efficient portfolio:

optimize_portfolio(annual_returns, 0.0003)

# Optimization terminated successfully.
#          Current function value: -7.829864
#          Iterations: 46
#          Function evaluations: 89

#    (array([ 0.76353353,  0.2103234 ,  0.02614307]), 7.8298640872716048)

# We are told that our best portfolio would have 76.4 percent AAPL, 21.0 percent KO, and 2.6 percent MSFT, and that portfolio would have a Sharpe ratio of 7.8298640872716048.


