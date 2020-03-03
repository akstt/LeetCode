class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: [[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        obstacleGrid[0][0] = 1
        h, w = len(obstacleGrid), len(obstacleGrid[0])
        for i in range(1, h):
            if obstacleGrid[i][0] == 0 and obstacleGrid[i-1][0] == 1:
                obstacleGrid[i][0] = 1
            else:
                obstacleGrid[i][0] = 0
        for i in range(1, w):
            if obstacleGrid[0][i] == 0 and obstacleGrid[0][i-1] == 1:
                obstacleGrid[0][i] = 1
            else:
                obstacleGrid[0][i] = 0
        for i in range(1, h):
            for j in range(1, w):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                else:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
        return obstacleGrid[-1][-1]
