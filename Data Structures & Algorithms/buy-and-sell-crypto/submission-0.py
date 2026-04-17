class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p = 0
        min_buy = prices[0]

        for price in prices:
            max_p = max(max_p, price - min_buy)
            min_buy = min(min_buy, price)
        
        return max_p
        