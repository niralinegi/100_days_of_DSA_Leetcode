class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        
        ans = 10000000
        
        memo = {}
        
        for currentCol in range(0, n):
            tempAns = self.minPathSum(matrix, 0, currentCol, m, n, memo)
            ans = min(ans, tempAns)
        return ans
    
    def minPathSum(self, matrix, currentRow, currentCol, m, n, memo):
        if currentCol < 0 or currentCol >= n:
            return 100001
        
        if currentRow == m-1:
            return matrix[currentRow][currentCol]
        
        currentKey = (currentRow, currentCol)
        
        if currentKey in memo:
            return memo[currentKey]
        
        leftDiagonal = matrix[currentRow][currentCol] + self.minPathSum(matrix, currentRow+1, currentCol-1, m, n, memo)
        down = matrix[currentRow][currentCol] + self.minPathSum(matrix, currentRow+1, currentCol, m, n, memo)
        rightDiagonal = matrix[currentRow][currentCol] + self.minPathSum(matrix, currentRow+1, currentCol+1, m, n, memo)
        
        memo[currentKey] = min(leftDiagonal, down, rightDiagonal)
        
        return memo[currentKey]
        