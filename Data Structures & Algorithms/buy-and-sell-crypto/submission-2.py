class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = float("inf"), float("-inf")

        for price in prices:
            buy = min(buy, price)
            sell = max(sell, price - buy)

        return sell
