# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 07:40:34 2022

@author: Nirali
"""

'''Knapsack with Duplicate Items: https://practice.geeksforgeeks.org/problems/knapsack-with-duplicate-items4201/1#
Given a set of N items, each with a weight and a value, represented by the array wt[] and val[] respectively. Also, a knapsack with weight limit W.
The task is to fill the knapsack in such a way that we can get the maximum profit. Return the maximum profit.
Note: Each item can be taken any number of times.'''


def knapSack(N, capacity, wt, val):
    dp = [[-1 for col in range(capacity+1)] for row in range(N)]
    return totalWays(0, N, capacity, wt, val, dp)

def totalWays(currentItem, N, capacity, wt, val, dp):
    if currentItem == N or capacity == 0:
        return 0
    
    currentItemWeight = wt[currentItem]
    currentProfit = val[currentItem]
    
    consider = 0
    
    key = (currentItem, capacity)
    
    if dp[currentItem][capacity] != -1:
        return dp[currentItem][capacity]
    
    if currentItemWeight <= capacity:
        consider = currentProfit + totalWays(currentItem, N, capacity-currentItemWeight, wt, val, dp)
        
    notConsider = totalWays(currentItem+1, N, capacity, wt, val, dp)
    
    dp[currentItem][capacity] = max(consider, notConsider)
    return dp[currentItem][capacity]


N = 2
capacity = 3
val = [1, 1]
wt = [2, 1]

print(knapSack(N, capacity, wt, val))