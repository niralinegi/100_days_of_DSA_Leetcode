# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 01:54:03 2022

@author: Nirali
"""

# 1137. N-th Tribonacci Number
# https://leetcode.com/problems/n-th-tribonacci-number/

class Solution:
    def tribonacci(self, n):
        memo = {}
        return self.trib(n, memo)
    
    def trib(self, n, memo):
        
        if n == 0:
            return 0
        
        if n in [1,2]:
            return 1
        
        key = n
        
        if key in memo:
            return memo[key]
        
        term_3 = self.trib(n-3, memo)
        term_2 = self.trib(n-2, memo)
        term_1 = self.trib(n-1, memo)
        
        memo[key] = term_3+term_2+term_1
        
        return memo[key]
        
s = Solution()
print(s.tribonacci(4))