class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        memo = {}
        return self.minSum(grid, 0, 0, len(grid), len(grid[0]), memo)
    
    def minSum(self, grid, currentRow, currentCol, m, n, memo):
        
        if currentRow == m-1 and currentCol == n-1:
            return grid[currentRow][currentCol]
        
        if currentRow >= m or currentCol >= n:
            return 100001
        
        key = (currentRow, currentCol)
        
        if key in memo:
            return memo[key]
        
        
        downMove = grid[currentRow][currentCol] + self.minSum(grid, currentRow+1, currentCol, m, n, memo)
        rightMove = grid[currentRow][currentCol] + self.minSum(grid, currentRow, currentCol+1, m, n, memo)
        
        memo[key] = min(downMove, rightMove)
        
        return memo[key]
