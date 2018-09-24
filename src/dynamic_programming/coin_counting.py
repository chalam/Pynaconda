def make_change_recursive(coinValueList, change):
    minCoins = change
    if change in coinValueList:
        return 1
    else:
        # get valid coin set which is less than change
        for i in [coin for coin in coinValueList if coin <= change]:
            # include the coin and adjust the change
            numCoins = 1 + make_change_recursive(coinValueList, change - i)
            if numCoins < minCoins:
                minCoins = numCoins
                print('change', change, 'in', minCoins)
    return minCoins


def make_change_memo(coinValueList, change, knownResults):
    minCoins = change
    if change in coinValueList:
        knownResults[change] = 1
        return 1
    elif knownResults[change] > 0:  # hit the cache
        return knownResults[change]
    else:
        for i in [coin for coin in coinValueList if coin <= change]:
            numCoins = 1 + make_change_memo(coinValueList,
                                            change - i, # include coin
                                            knownResults)
            if numCoins < minCoins:
                minCoins = numCoins
                knownResults[change] = minCoins  # save to cache
    return minCoins


def make_change_dp(coinValueList, change, minCoins):
    """optimal count of change"""
    for cents in range(change + 1):
        print('cents', cents)
        coinCount = cents
        for j in [c for c in coinValueList if c <= cents]:
            coinCount = min(coinCount, minCoins[cents - j] + 1)
            print('coinCount', j, coinCount)
        minCoins[cents] = coinCount
    return minCoins[change]


def make_change_dp2(coinValueList, change, minCoins, coinsUsed):
    """optimal count of change and coins used preserved"""
    for cents in range(change + 1):
        coinCount = cents
        newCoin = 1
        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents - j] + 1 < coinCount:
                coinCount = minCoins[cents - j] + 1
                newCoin = j
        minCoins[cents] = coinCount
        coinsUsed[cents] = newCoin
    return minCoins[change]


def printCoins(coinsUsed, change):
    coin = change
    while coin > 0:
        thisCoin = coinsUsed[coin]
        print(thisCoin)
        coin = coin - thisCoin


import time

start = time.time()
amount = 63  # 0 sec
clist = [1, 5, 10, 21, 25]  # fictional 21 cent
print(make_change_memo(clist, amount, [0] * (amount + 1)))
print('make_change_memo', time.time() - start, 'seconds')

start = time.time()
amount = 63  # 0 sec
amnt = 63
coinsUsed = [0] * (amnt + 1)
coinCount = [0] * (amnt + 1)

print("Making change for", amnt, "requires")
print('make_change_dp', make_change_dp(clist, amnt, [0] * (amnt + 1)))
print('make_change_dp2', make_change_dp2(clist, amnt, coinCount, coinsUsed), "coins")
print("They are:")
printCoins(coinsUsed, amnt)
print("The used list is as follows:")
print(coinsUsed)
print('make_change_dp', time.time() - start, 'seconds')

start = time.time()
# amount = 63 # 36.8524 sec  67,716,925 recursive calls
amount = 15
print(make_change_recursive([1, 5, 10, 25], amount))
print('make_change_recursive', time.time() - start, 'seconds')
