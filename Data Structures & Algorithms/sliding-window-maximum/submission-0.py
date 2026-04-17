class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque([])
        l = 0
        ans = []

        for r, num in enumerate(nums):
            while q and q[0][0] < l:
                q.popleft()
            
            while q and q[-1][1] < num:
                q.pop()

            q.append((r, num))

            if (r - l + 1) == k:
                ans.append(q[0][1])
                l += 1
        
        return ans