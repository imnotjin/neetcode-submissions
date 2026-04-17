class Solution:
    def numSquares(self, n: int) -> int:
        q = deque([(n, 0)])
        
        while q:
            num, count = q.popleft()

            if num < 0:
                continue
            if num == 0:
                return count
            
            for base in range(int(math.sqrt(num)), 0, -1):
                q.append((num - base ** 2, count + 1))
                




                
