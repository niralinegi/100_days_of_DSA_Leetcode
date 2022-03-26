# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 10:16:35 2022

@author: Nirali
"""

# https://www.geeksforgeeks.org/find-number-valid-parentheses-expressions-given-length/
'''
Given a number n find the number of valid parentheses expressions of that length. 
Examples : 
 

Input: 2
Output: 1 
There is only possible valid expression of length 2, "()"

Input: 4
Output: 2 
Possible valid expression of length 4 are "(())" and "()()" 

Input: 6
Output: 5
Possible valid expressions are ((())), ()(()), ()()(), (())() and (()())
'''

class Solution:
    
    def findCatalan(self,n):
        
        memo = {}
        return self.nthCatalan(n//2, memo)
        
    def nthCatalan(self, n, memo):
        
        if n == 0 or n == 1:
            return 1
            
        ways = 0
        key = n
        
        if key in memo:
            return memo[key]
            
        for i in range(0, n):
            ways += self.nthCatalan(i, memo) * self.nthCatalan(n-i-1, memo)
            
        memo[key] = ways
        return memo[key]
    
    
s = Solution()
print(s.findCatalan(6))