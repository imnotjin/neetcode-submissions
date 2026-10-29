class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = float('inf')
        maxi = float('-inf')

        for price in prices:
            mini = min(mini, price)
            maxi = max(maxi, price - mini)
        
        return maxi