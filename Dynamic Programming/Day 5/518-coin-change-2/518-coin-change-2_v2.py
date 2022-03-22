class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[-1 for col in range(amount+1)] for row in range(len(coins))]
        return self.totalWays(amount, coins, 0, dp)
    
    def totalWays(self, amount, coins, currentItem, dp):
        if amount == 0:
            return 1
        
        if currentItem == len(coins):
            return 0
        
        if dp[currentItem][amount] != -1:
            return dp[currentItem][amount]
        
        consider = 0
        
        if coins[currentItem] <= amount:
            consider = self.totalWays(amount-coins[currentItem], coins, currentItem, dp)
            
        notConsider = self.totalWays(amount, coins, currentItem+1, dp)
        
        dp[currentItem][amount] = consider+notConsider
        return dp[currentItem][amount]
        
        
