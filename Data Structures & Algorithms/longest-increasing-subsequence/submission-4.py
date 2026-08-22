class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # if not nums: return 0
        # n = len(nums)
        # dp = [1] * n
        # for i in range(1, n):
        #     for j in range(i):
        #         if nums[i] > nums[j]:
        #             dp[i] = max(dp[i], dp[j] + 1)
        # return max(dp)

        tails = []
        for x in nums:
            low, high = 0, len(tails)
            while low < high:
                mid = (low + high) // 2
                if tails[mid] < x:
                    low = mid + 1
                else:
                    high = mid
            
            if low == len(tails):
                tails.append(x)
            else:
                tails[low] = x
        return len(tails)
        