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
        # import bisect
        def bisect_left(a, x, lo, hi=None, key=None):
            if not hi:
                hi = len(a)

            while lo < hi:
                mid = (lo + hi) // 2
                if key(a[mid]) < x:
                    lo = mid + 1
                else:
                    hi = mid
            return a[lo]

        return bisect_left(
            range(1, max(piles) + 1),
            True,
            0,
            key=lambda k: sum(math.ceil(pile / k) for pile in piles) <= h
        )
