class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        return self.maximumProfit(prices, 0, 1, 1, memo)
    
    def maximumProfit(self, prices, currentDay, canBuy, transCount, memo):
        if currentDay >= len(prices) or transCount == 0:
            return 0
        
        currentKey = (currentDay, canBuy, transCount)
        
        if currentKey in memo:
            return memo[currentKey]
        
        if canBuy == 1:
            idle = self.maximumProfit(prices, currentDay+1, canBuy, 1, memo)
            buy = -prices[currentDay] + self.maximumProfit(prices, currentDay+1, 0, 1, memo)
            ans = max(idle, buy)
        else:
            idle = self.maximumProfit(prices, currentDay+1, canBuy, 1, memo)
            sell = prices[currentDay] + self.maximumProfit(prices, currentDay+1, 1, 0, memo)
            ans = max(idle, sell)
            
        memo[currentKey] = ans
        return memo[currentKey] 
                
