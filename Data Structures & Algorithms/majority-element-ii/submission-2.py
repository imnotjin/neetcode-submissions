class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1

            if len(counts) <= 2:
                continue
            
            new_counts = defaultdict(int)
            for k, v in counts.items():
                if v > 1:
                    new_counts[k] = v - 1
            counts = new_counts
        
        return [k for k in counts if nums.count(k) > len(nums) // 3]
        