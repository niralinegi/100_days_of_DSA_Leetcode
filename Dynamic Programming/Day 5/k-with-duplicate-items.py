#User function Template for python3

import sys
sys.setrecursionlimit(10**6)

class Solution:
    def knapSack(self, N, capacity, val, wt):
        # code here
        dp = [[-1 for col in range(capacity+1)]
            for row in range(N)]
        
        return self.maxProfit(wt, val, 0, capacity, N, dp)
        
    def maxProfit(self, wt, val, current_item, capacity, N, dp):

        if capacity == 0 or current_item == N:
            return 0
            
        current_weight = wt[current_item]
        current_profit = val[current_item]
        
        consider = 0
        
        key = (current_item, capacity)
        if dp[current_item][capacity] != -1:
            return dp[current_item][capacity]
        
        if current_weight <= capacity:
            consider = current_profit + self.maxProfit(wt, val, current_item, capacity-current_weight, N, dp)
            
        notConsider = self.maxProfit(wt, val, current_item+1, capacity, N, dp)
        
        dp[current_item][capacity] = max(consider, notConsider)
        return dp[current_item][capacity]

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, W = [int(x) for x in input().split()]
        val = input().split()
        for itr in range(N):
            val[itr] = int(val[itr])
        wt = input().split()
        for it in range(N):
            wt[it] = int(wt[it])
        
        ob = Solution()
        print(ob.knapSack(N, W, val, wt))
# } Driver Code Ends
