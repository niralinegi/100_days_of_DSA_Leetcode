class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        return self.totalWays(0, 0, m, n, memo)
    
    def totalWays(self, currentRow, currentCol, m, n, memo):
        
        if currentRow == m-1 and currentCol == n-1:
            return 1
        
        if currentRow >= m or currentCol >= n:
            return 0
        
        key = (currentRow, currentCol)
        
        if key in memo:
            return memo[key]
        
        moveRight = self.totalWays(currentRow, currentCol+1, m, n, memo)
        moveDown = self.totalWays(currentRow+1, currentCol, m, n, memo)
        
        memo[key] = moveRight+moveDown
        
        return memo[key]