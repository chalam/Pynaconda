# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
# https://codesays.com/?s=stock

# Design an algorithm to find the maximum profit.
# You may complete at most k transactions.

import heapq


class TopN:
    def __init__(self, n):
        assert (n > 0)
        self.maximum = n
        self.content = []

    def add(self, value):
        if len(self.content) < self.maximum:
            heapq.heappush(self.content, value)
        elif self.content[0] < value:
            heapq.heappushpop(self.content, value)

    def result(self):
        return self.content

    def debug_info(self):
        print("Content(max:", self.maximum, "):", self.content)


def maxProfit(prices, k):
    if len(prices) < 2 or k < 1:     return 0
    stack = []
    profitable = TopN(k)
    valley = 0
    peak = -1
    while valley < len(prices):
        # Find the next profitable transaction.
        while valley < len(prices) - 1 and prices[valley] >= prices[valley + 1]:
            valley += 1
        if valley == len(prices) - 1:        break
        peak = valley + 1
        while peak < len(prices) - 1 and prices[peak] < prices[peak + 1]:
            peak += 1
        # Try to finalize or combine with previous transactions.
        valley_price = prices[valley]
        peak_price = prices[peak]
        while len(stack) != 0 and stack[-1][0] >= valley_price:
            transaction = stack.pop()
            profitable.add(transaction[1] - transaction[0])
        while len(stack) != 0 and stack[-1][1] <= peak_price:
            transaction = stack.pop()
            profitable.add(transaction[1] - valley_price)
            valley_price = transaction[0]
        # Finish processing current transaction.
        stack.append([valley_price, peak_price])
        valley = peak + 1
    # Finalize all the remaining transactions.
    for transaction in stack:
        profitable.add(transaction[1] - transaction[0])
    return sum(profitable.result())


assert maxProfit([5, 3, 2], 3) == 0
assert maxProfit([2, 4, 1], 2) == 2
assert maxProfit([3, 2, 6, 5, 0, 3], 2) == 7
