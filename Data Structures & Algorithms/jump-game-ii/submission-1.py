class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        q = deque([(0, 0)])
        v = set()
        v.add(0)

        while q:
            i, jumps = q.popleft()

            if i == n - 1:
                return jumps
            
            for j in range(1, nums[i] + 1):
                if i + j < n and i + j not in v:
                    q.append((i + j, jumps + 1))
                    v.add(i + j)
        
        return 0
