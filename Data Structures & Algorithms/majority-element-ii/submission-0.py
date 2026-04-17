class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        return [k for k in count.keys() if count[k] > (len(nums) // 3)]
