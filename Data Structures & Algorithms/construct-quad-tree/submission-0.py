"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        ans = []
        
        def dfs(n, r, c):
            if all(grid[row][col] == grid[r][c] for row in range(r, r + n) for col in range(c, c + n)):
                return Node(grid[r][c], True)

            n = n // 2
            top_left = dfs(n, r, c)
            top_right = dfs(n, r, c + n)
            bottom_left = dfs(n, r + n, c)
            bottom_right = dfs(n, r + n, c + n)

            return Node(0, False, top_left, top_right, bottom_left, bottom_right)
        
        return dfs(len(grid), 0, 0) # size, top-left corner
