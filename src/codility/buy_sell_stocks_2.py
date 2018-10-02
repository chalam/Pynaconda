import sys
# MLP

def maximize_buy_low_sell_high(prices):
    min_price = sys.maxsize
    max_profit = 0
    for i, price in enumerate(prices):
        min_price = min(min_price, price)
        if max_profit < price-min_price:
            max_profit = price - min_price
            max_idx = i
        print(i, price, min_price, max_profit)
    return max_profit, max_idx

# prices = [10, 7, 5, 8, 11, 9]
# print(maximize_buy_low_sell_high(prices))
#
# prices = make_arrary()
# print(prices, maximize_buy_low_sell_high(prices))


def maximize_profit(prices, n):
    """
        make a dp array holding the end index for sell
    :param prices:
    :param n:
    :return:
    """
    dp = [0] * n
    dp[0] = -1
    for i in range(1, n):
        j = i - 1
        while prices[j] < prices[i] and dp[j] != -1:
            j = dp[j]
        if prices[j] > prices[i]:
            dp[i] = j
        else:
            dp[i] = dp[j]
    print(dp)
    return trade_buy_sell(prices, n, dp)

def trade_buy_sell(prices, n, dp):
    """
        use the dp array to buy and sell at giving idx
    :param prices:
    :param n:
    :param dp:
    :return:
    """
    pnl = 0
    i = n - 1
    while i > 0:
        end = i
        start = dp[i] + 1
        for j in range(start, end):
            pnl += prices[end] - prices[j]
        i = dp[i]
    print(pnl)
    return pnl


def maximize_profit2(prices, n):
    """
        find the max price so far from the end
        profit is the diff of current price and max price so far
        aggregate profit
    :param prices:
    :param n:
    :return:
    """
    profit = 0
    max_price = 0
    for i in range(n-1, -1, -1):
        max_price = max(prices[i], max_price)
        profit += max_price - prices[i]
        print(i, prices[i], max_price, profit)
    return profit


assert maximize_profit([5, 3, 2], 3) == 0
assert maximize_profit([1, 2, 100], 3) == 197
assert maximize_profit([1, 3, 1, 2], 4) == 3

assert maximize_profit2([5, 3, 2], 3) == 0
assert maximize_profit2([1, 2, 100], 3) == 197
assert maximize_profit2([1, 3, 1, 2], 4) == 3
assert maximize_profit2([5, 4, 3, 4, 5], 5) == 4

# long int **J;
#
# long int InvestReturn(long int i,long int x,long int *p,long int N){
# if (i==N) {
#     J[N][x]=0;
#     return 0;
# }
# if (J[i][x]!=-1) {
#     return J[i][x];
# }
# long int A =InvestReturn(i+1,1,p,N)   -InvestReturn(i+1,0,p,N);
# long int B =InvestReturn(i+1,0,p,N);
#
# if (A-p[i]>0) { //buying one stock is opt.
#     J[i][x] = -p[i]+A*(x+1)+B;
#     return J[i][x];
# }else{ //selling all x stocks is optimal
#     J[i][x] = x*p[i]+B;
#     return J[i][x];
# }