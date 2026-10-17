class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        def can(k):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)
                if hours > h:
                    return False
            return True

        while l < r:
            k = (l + r) // 2
            if can(k):
                r = k
            else:
                l = k + 1
        return l
