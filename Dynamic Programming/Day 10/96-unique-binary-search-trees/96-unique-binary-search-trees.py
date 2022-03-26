class Solution:
    def numTrees(self, n: int) -> int:
        memo = {}
        return self.totalWays(n, memo)
    
    def totalWays(self, n, memo):
        
        if n == 0 or n == 1:
            return 1
        
        ways = 0
        key = n
        
        if key in memo:
            return memo[key]
        
        for i in range(0, n):
            ways += self.totalWays(i, memo) * self.totalWays(n-i-1, memo)
            
        memo[key] = ways
        return memo[key]
