class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # n = len(nums)
        # res = 0
        # prefix = [0] * (n + 1)
        # for i in range(n):
        #     prefix[i + 1] = prefix[i] + nums[i]
        # for i in range(n):
        #     for j in range(i, n):
        #         if prefix[j+1] - prefix[i] == k:
        #             res += 1
        # return res
        c = defaultdict(int)
        c[0] = 1
        curr = res = 0
        for num in nums:
            curr += num
            res += c[curr - k]
            c[curr] += 1
        return res
