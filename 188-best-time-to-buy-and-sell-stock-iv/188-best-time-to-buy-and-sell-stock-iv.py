class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        memo = {}
        return self.maximumProfit(prices, 0, 1, k, memo)
    
    def maximumProfit(self, prices, currentIndex, canBuy, transCount, memo):
        if currentIndex >= len(prices) or transCount == 0:
            return 0
        
        key = (currentIndex, canBuy, transCount)
        
        if key in memo:
            return memo[key]
        
        ans = 0
        
        if canBuy == 1:
            idle = self.maximumProfit(prices, currentIndex+1, canBuy, transCount, memo)
            buy = -prices[currentIndex] + self.maximumProfit(prices, currentIndex+1, 0, transCount, memo)
            ans = max(idle, buy)
            
        else:
            idle = self.maximumProfit(prices, currentIndex+1, canBuy, transCount, memo)
            sell = prices[currentIndex] + self.maximumProfit(prices, currentIndex+1, 1, transCount-1, memo)
            ans = max(idle, sell)
            
        memo[key] = ans
        
        return memo[key]
        