class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1

            if len(counts) <= 2:
                continue
            
            for k in list(counts.keys()):
                counts[k] -= 1
                if counts[k] == 0:
                    del counts[k]
        
        return [k for k in counts if nums.count(k) > len(nums) // 3]
        