class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l < r:
            mid = (l + r) // 2
            hours = sum(math.ceil(pile / mid) for pile in piles)

            if hours <= h:
                res = mid
                r = mid
            else:
                l = mid + 1
        
        return res
