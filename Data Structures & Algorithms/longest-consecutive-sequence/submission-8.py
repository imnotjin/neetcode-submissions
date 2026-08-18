class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nset = set(nums)
        ans = 0

        for num in nset:
            if num - 1 in nset:
                continue

            temp = num
            streak = 1
            while temp + 1 in nset:
                temp += 1
                streak += 1
            
            ans = max(ans, streak)
            print(ans)
        
        return ans
