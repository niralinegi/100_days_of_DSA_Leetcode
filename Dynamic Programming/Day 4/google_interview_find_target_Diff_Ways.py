# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 21:56:30 2022

@author: Nirali
"""

# Google Interview: Count no of subsets with given difference
'''

s1-s2 = x (x is diff) - (1)
s1+s2 = s -(2)
rewriting (1)
x+s2 + s2 = s
2s2 = s-x
s2 = (s-x)/2
'''
nums = [1,1,2,3]
diff = 1

def findTargetDiffWays(nums, diff):
    total = sum(nums)
    memo = {}
    return totalWays(0, nums, diff, (total-diff)//2, memo)

def totalWays(currentIndex, nums, diff, totsum, memo):
    if currentIndex == len(nums) and totsum == 0:
        return 1
    
    if currentIndex >= len(nums) and totsum != 0:
        return 0
    
    currentKey = (currentIndex, totsum)
    
    if currentKey in memo:
        return memo[currentKey]
    
    consider = totalWays(currentIndex+1, nums, diff, totsum-nums[currentIndex], memo)
    notconsider = totalWays(currentIndex+1, nums, diff, totsum, memo)
    
    memo[currentKey] = (consider+notconsider)
    
    return memo[currentKey]
    
print(findTargetDiffWays(nums, diff))