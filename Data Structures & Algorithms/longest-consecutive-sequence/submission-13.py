class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0

        for n in s:
            if n - 1 in s:
                continue
            temp = n
            streak = 1
            while temp + 1 in s:
                temp += 1
                streak += 1
            res = max(res, streak)
        return res
