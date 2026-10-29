class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cand, cnt = None, 0
        for num in nums:
            if num == cand:
                cnt += 1
            elif cnt == 0:
                cand, cnt = num, 1
            else:
                cnt -= 1
        return cand