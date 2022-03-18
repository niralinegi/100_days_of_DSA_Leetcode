# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 18:41:14 2022

@author: Nirali
"""

# Runtime: 24 ms, faster than 98.91% of Python3 online submissions for Fibonacci Number.
# Memory Usage: 13.8 MB, less than 67.31% of Python3 online submissions for Fibonacci Number.

# 509. Fibonacci Number

class Solution:
    def fib(self, n: int) -> int:
        return self.calc_fibno(n,{})
    
    def calc_fibno(self, n, memo):
        if n < 2:
            return n
        
        key = n
        if key in memo:
            return memo[key]
        
        prev_prev_num = self.calc_fibno(n-2, memo)
        prev_num = self.calc_fibno(n-1, memo)
        memo[key] = prev_prev_num + prev_num
        
        return memo[key]
        
        
        
s = Solution()
print(s.fib(4))