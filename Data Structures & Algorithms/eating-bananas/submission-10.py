class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can(k):
            x = 0
            for p in piles:
                x += math.ceil(p / k)
                if x > h:
                    return False
            return True

        l, r = 1, max(piles)
        while l < r:
            k = (l + r) // 2
            if can(k):
                r = k
            else:
                l = k + 1
        return l