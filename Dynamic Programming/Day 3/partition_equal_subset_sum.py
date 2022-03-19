# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 15:35:47 2022

@author: Nirali
"""
#416. Partition Equal Subset Sum
#https://leetcode.com/problems/partition-equal-subset-sum/
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        if totalSum%2:
            return False
        memo = {}
        return self.isPossible(0, nums, totalSum//2, memo)
    def isPossible(self, currentIndex, nums, targetSum, memo):
        if targetSum == 0:
            return True
        if currentIndex >= len(nums):
            return False
        
        key = (currentIndex, targetSum)
        
        if key in memo:
            return memo[key]
        
        consider = False
        
        if nums[currentIndex] <= targetSum:
            consider = self.isPossible(currentIndex+1, nums, targetSum-nums[currentIndex], memo)
            if consider:
                return True 
        not_consider = self.isPossible(currentIndex+1, nums, targetSum, memo)
        memo[key] = (consider or not_consider)
        return memo[key]
        
s = Solution()
nums = [1,5,11,5]
print(s.canPartition(nums))