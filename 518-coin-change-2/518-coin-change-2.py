class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        return self.totalWays(amount, coins, 0, {})
    
    def totalWays(self, amount, coins, currentIndex, memo):
        if amount == 0:
            return 1
        
        if currentIndex == len(coins):
            return 0
        
        currentKey = (currentIndex, amount)
        
        if currentKey in memo:
            return memo[currentKey]
        
        consider = 0
        
        if coins[currentIndex] <= amount:
            consider = self.totalWays(amount-coins[currentIndex], coins, currentIndex, memo)
            
        notConsider = self.totalWays(amount, coins, currentIndex+1, memo)
        
        memo[currentKey] = consider+notConsider
        return memo[currentKey]
        
        