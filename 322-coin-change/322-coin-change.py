class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [[-1 for col in range(amount+1)] for row in range(len(coins))]
        ans = self.minCoins(coins, amount, 0, dp)
        if ans == 10001:
            return -1
        else:
            return ans
    
    def minCoins(self, coins, amount, currentIndex, dp):
        if currentIndex == len(coins):
            return 10001
        
        if amount == 0:
            return 0
        
        currentCoin = coins[currentIndex]
        
        consider = 10001
        if dp[currentIndex][amount] != -1:
            return dp[currentIndex][amount] 
        
        if currentCoin <= amount:
            consider = 1 + self.minCoins(coins, amount-currentCoin, currentIndex, dp)
            
        notConsider = self.minCoins(coins, amount, currentIndex+1, dp)
        
        dp[currentIndex][amount] = min(consider, notConsider)
        return dp[currentIndex][amount]
            
        