class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        memo = {}
        return self.totalWays(0, 0, len(obstacleGrid), len(obstacleGrid[0]), obstacleGrid, memo)
    
    def totalWays(self, currentRow, currentCol, m, n, obstacleGrid, memo):
        
        if currentRow >= m or currentCol >= n or obstacleGrid[currentRow][currentCol] == 1:
            return 0
        
        if currentRow == m-1 and currentCol == n-1:
            return 1
        
        key = (currentRow, currentCol)
        
        if key in memo:
            return memo[key]
        
        moveRight = self.totalWays(currentRow, currentCol+1, m, n, obstacleGrid, memo)
        moveDown = self.totalWays(currentRow+1, currentCol, m, n, obstacleGrid, memo)
        
        memo[key] = moveRight+moveDown
        
        return memo[key]