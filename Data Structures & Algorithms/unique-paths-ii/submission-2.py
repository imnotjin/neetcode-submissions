class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        grid = [[0] * n for _ in range(m)]

        if obstacleGrid[0][0]:
            return 0
        grid[0][0] = 1

        for i in range(1, m):
            if obstacleGrid[i][0]:
                break
            grid[i][0] = 1
        
        for j in range(1, n):
            if obstacleGrid[0][j]:
                break
            grid[0][j] = 1
        
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j]:
                    grid[i][j] = 0
                else:
                    grid[i][j] = grid[i-1][j] + grid[i][j-1]
        
        return grid[m-1][n-1]
