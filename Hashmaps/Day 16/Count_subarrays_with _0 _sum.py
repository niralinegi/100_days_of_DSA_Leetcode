# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 09:09:35 2022

@author: Nirali
"""

# Count subarrays with 0 sum

# Problem Statement
# You are given ‘N’ integers in the form of an array ‘ARR’. Count the number of subarrays having their sum as 0.
# For Example :
# Let ‘ARR’ be: [1, 4, -5]
# The subarray [1, 4, -5] has a sum equal to 0. So the count is 1.

from typing import List

def countSubarrays(n: int, arr: List[int]) -> int:
    # Write your code here.
    memo = {}
    prefixSum = 0
    answer = 0
    memo[prefixSum] = 1
    
    for i in range(0, n):
        prefixSum += arr[i]
        
        if prefixSum in memo:
            answer += memo[prefixSum]
            memo[prefixSum] = memo[prefixSum] + 1
        else:
            memo[prefixSum] = 1
            
    return answer

arr = [1, 4, -5]
print(countSubarrays(3, arr))