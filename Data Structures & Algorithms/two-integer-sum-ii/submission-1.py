class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        l, r = 1, n

        while l < r:
            add = numbers[l - 1] + numbers[r - 1]

            if add == target:
                return [l, r]
            
            if add > target:
                r -= 1
            else:
                l += 1
        
        return -1
