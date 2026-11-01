class Solution:
    def countBits(self, n: int) -> List[int]:

        def count(i):
            res = 0
            while i:
                i &= i - 1
                res += 1
            return res
        return [count(i) for i in range(n + 1)]