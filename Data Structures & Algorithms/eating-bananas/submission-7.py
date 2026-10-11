class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # for i in range(1, max(piles)):
        #     if sum(math.ceil(pile / i) for pile in piles) <= h:
        #         return i
        # return max(piles)

        l, r = 1, max(piles) + 1
        while l < r:
            k = (l + r) // 2
            if sum(math.ceil(pile / k) for pile in piles) <= h:
                r = k
            else:
                l = k + 1
        
        return l
