class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        window = deque()

        l = 0
        for r, num in enumerate(nums):
            while window and window[0][0] < l:
                window.popleft()
            while window and window[-1][1] <= num:
                window.pop()
            window.append((r, num))
            if r - l + 1 == k:
                res.append(window[0][1])
                l += 1
        
        return res
