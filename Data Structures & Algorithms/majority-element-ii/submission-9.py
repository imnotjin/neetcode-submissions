class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1

            if len(freq) <= 2:
                continue
            
            new_freq = defaultdict(int)
            for x, f in freq.items():
                if f > 1:
                    new_freq[x] = f - 1
            freq = new_freq
        
        return [num for num in freq if nums.count(num) > len(nums) // 3]