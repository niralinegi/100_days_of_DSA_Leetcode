# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 18:32:35 2022

@author: Nirali
"""
# https://leetcode.com/problems/climbing-stairs/
# Calculate the total ways to climb the top of staircase if can take 1 jump or 2 jump

def climbStairs(n):
    return total_ways(0,n,{})

def total_ways(currentStair, targetStair, memo):
    if currentStair == targetStair:
        return 1
    
    if currentStair > targetStair:
        return 0
    
    currentKey = currentStair
    
    if currentKey in memo:
        return memo[currentKey]
    
    oneJump = total_ways(currentStair+1, targetStair, memo)
    twoJump = total_ways(currentStair+2, targetStair, memo)
    
    totalJump = oneJump+twoJump
    
    memo[currentKey] = totalJump
    return totalJump

print(climbStairs(3))
