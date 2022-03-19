# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 13:14:43 2022

@author: Nirali
"""

# 0 - 1 Knapsack Problem
# https://practice.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1#
class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,capacity, wt, val, n):
        memo = {}
        return self.maxProfit(wt, val, 0, capacity, n, memo)
        # code here
    def maxProfit(self, weights, profits, currentItem, capacity, n, memo):
        if currentItem == n:
            return 0
            
        currentItemWeight = weights[currentItem]
        currentItemProfit = profits[currentItem]
        
        currentKey = str(currentItem)+'-'+str(capacity)
        if currentKey in memo:
            return memo[currentKey]
        
        consider = 0
        if currentItemWeight <= capacity:
            consider = currentItemProfit + self.maxProfit(weights, profits, currentItem+1, capacity-currentItemWeight, n, memo)
            
        notconsider = self.maxProfit(weights, profits, currentItem+1, capacity, n, memo)
        
        memo[currentKey] = max(consider, notconsider)
        
        return memo[currentKey]  
    
s = Solution()
N = 3
W = 4
values = [1,2,3]
weight = [4,5,1]
print(s.knapSack(W, weight, values, N))