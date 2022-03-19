# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 10:52:35 2022

@author: Nirali
"""
# 213. House Robber II
# https://leetcode.com/problems/house-robber-ii/submissions/

class Solution:
    def rob(self, nums):
        memo1 = {}
        memo2 = {}
        if len(nums) == 1:
            return nums[0]
        return max(self.total_money(0, len(nums)-1, nums, memo1), self.total_money(1, len(nums), nums, memo2))
    
    def total_money(self, current_house, last_house, nums, memo):
        
        if current_house >= last_house:
            return 0
        
        current_key = current_house
        
        if current_key in memo:
            return memo[current_key]
        
        rob = nums[current_house] + self.total_money(current_house+2, last_house, nums, memo)
        norob = self.total_money(current_house+1, last_house, nums, memo)
     
        memo[current_key] = max(rob, norob)
       
        return memo[current_key]
    
s = Solution()
nums = [2,3,2]
print(s.rob(nums)) 