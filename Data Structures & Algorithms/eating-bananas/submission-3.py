class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # l, r = 1, max(piles) + 1
        # res = r
        # while l < r:
        #     mid = (l + r) // 2
        #     hours = sum(math.ceil(pile / mid) for pile in piles)

        #     if hours <= h:
        #         res = mid
        #         r = mid
        #     else:
        #         l = mid + 1
        
        # return res
        import bisect
        return bisect.bisect_left(
            range(1, max(piles) + 1),
            True,
            key=lambda k: sum(math.ceil(pile / k) for pile in piles) <= h
        ) + 1
