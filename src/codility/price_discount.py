import heapq

def find_lower_or_equal(prices, start, m):
    for i in range(start, len(prices)):
        if prices[i] <= m:
            return prices[i]
    return None

def finalPrice(prices):
    """
        find the lower ar equal and discount it
        O(N^2)
    :param prices:
    :return:
    """
    print(prices)
    n = len(prices)
    no_changed_indexes = []
    final_prices = []
    for i in range(n - 1):
        next_lower_equal = find_lower_or_equal(prices, i+1, prices[i])
        print(i, prices[i], next_lower_equal, next_lower_equal, final_prices, no_changed_indexes)
        if next_lower_equal is None:
            final_prices.append(prices[i])
            no_changed_indexes.append(i)
        else:
            final_prices.append(prices[i] - next_lower_equal)

    final_prices.append(prices[n - 1])
    no_changed_indexes.append(n - 1)
    print(sum(final_prices))
    print(' '.join(map(str, no_changed_indexes)))
    return sum(final_prices), no_changed_indexes

if __name__ == '__main__':
    prices = [5, 1, 3, 4, 6, 2]
    cost, items  = finalPrice(prices)
    assert cost == 14
    assert items == [1, 5]
    prices = [1, 3, 3, 2, 5]
    cost, items  = finalPrice(prices)
    assert cost == 9
    assert items == [0, 3, 4]

