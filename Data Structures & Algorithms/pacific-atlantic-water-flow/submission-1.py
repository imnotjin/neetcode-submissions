class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        
        ROWS, COLS = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()
        
        def bfs(queue, visited):
            while queue:
                r, c = queue.popleft()
                visited.add((r, c))
                
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < ROWS and 0 <= nc < COLS and 
                        (nr, nc) not in visited and 
                        heights[nr][nc] >= heights[r][c]):  # Flow upward!
                        queue.append((nr, nc))
                        visited.add((nr, nc))
        
        # Start BFS from Pacific borders (top + left)
        pacific_queue = deque()
        for c in range(COLS):
            pacific_queue.append((0, c))  # Top row
        for r in range(ROWS):
            pacific_queue.append((r, 0))  # Left column
        bfs(pacific_queue, pacific)
        
        # Start BFS from Atlantic borders (bottom + right)
        atlantic_queue = deque()
        for c in range(COLS):
            atlantic_queue.append((ROWS - 1, c))  # Bottom row
        for r in range(ROWS):
            atlantic_queue.append((r, COLS - 1))  # Right column
        bfs(atlantic_queue, atlantic)
        
        # Find intersection
        return [[r, c] for r, c in pacific & atlantic]