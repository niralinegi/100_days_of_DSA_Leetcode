class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        memo = {}
        return self.totalWays(n, k, target, memo)
    
    def totalWays(self, n, k, target, memo):
        
        if n == 0 and target == 0:
            return 1
        
        if n == 0 or target <= 0:
            return 0
        
        ways = 0
        MOD = 1000000007
        
        currentKey = (n, target)
        
        if currentKey in memo:
            return memo[currentKey]
        
        for dice in range(1, k+1):
            tempAns = self.totalWays(n-1, k, target-dice, memo) % MOD
            ways = ways % MOD
            ways = (ways + tempAns) % MOD
            
        memo[currentKey] = ways
        return memo[currentKey]
            
            