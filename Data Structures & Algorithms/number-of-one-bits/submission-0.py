class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        for power in range(33):
            if (2 ** power) & n:
                count += 1
        
        return count
