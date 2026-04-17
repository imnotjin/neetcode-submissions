class Solution:
    def numSquares(self, n: int) -> int:
        q = deque([(n, 0)])
        s = set()
        s.add(n)
        
        while q:
            num, count = q.popleft()

            if num < 0:
                continue
            if num == 0:
                return count
            
            for base in range(int(math.sqrt(num)), 0, -1):
                nxt = num - base ** 2
                if nxt not in s:
                    q.append((nxt, count + 1))
                    s.add(nxt)
