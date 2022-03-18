# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 01:39:36 2022

@author: Nirali
"""

# 198. House Robber 
# https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums):
        memo = {}
        return self.maxMoney(0, nums, memo)
    
    def maxMoney(self, currentHouse, nums, memo):
        if currentHouse >= len(nums):
            return 0
        
        currentKey = currentHouse
        
        if currentKey in memo:
            return memo[currentKey]
        
        rob = nums[currentHouse] + self.maxMoney(currentHouse+2, nums, memo)
        no_rob = self.maxMoney(currentHouse+1, nums, memo)
        
        memo[currentKey] = max(rob, no_rob)
        
        return memo[currentKey]
    
s = Solution()
nums = [1,2,3,1]
print(s.rob(nums))  
        