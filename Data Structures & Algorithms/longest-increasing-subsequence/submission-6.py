import bisect

class Solution:
    # def bisect_left(self, nums, x, lo, hi):
    #     while lo < hi:
    #         mid = (lo + hi) // 2
    #         if nums[mid] < x:
    #             lo = mid + 1
    #         else:
    #             hi = mid
    #     return lo

    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = []
        for x in nums:
            # idx = self.bisect_left(tails, x, 0, len(tails))
            idx = bisect.bisect_left(tails, x)
            if idx == len(tails):
                tails.append(x)
            else:
                tails[idx] = x
        return len(tails)
