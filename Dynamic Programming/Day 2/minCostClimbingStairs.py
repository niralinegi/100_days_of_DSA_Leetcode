# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 01:02:44 2022

@author: Nirali
"""
# 746. Min Cost Climbing Stairs https://leetcode.com/problems/min-cost-climbing-stairs/

class Solution:
    def minCostClimbingStairs(self, cost):
        memo = {}
        return min(self.min_cost(cost, 0, memo), memo[1])
    
    def min_cost(self, cost, current_index, memo):
        
        if current_index == len(cost):
            return 0
        if current_index > len(cost):
            return 1001
        
        current_key = current_index
        
        if current_key in memo:
            return memo[current_key]
        
        oneJump = cost[current_index]+ self.min_cost(cost, current_index+1, memo)
        twoJump = cost[current_index]+ self.min_cost(cost, current_index+2, memo)
        
        memo[current_key] = min(oneJump, twoJump)
        
        return memo[current_key]
    
    
s = Solution()
cost = [10,15,20]
print(s.minCostClimbingStairs(cost))
        