# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 11:17:55 2022

@author: Nirali
"""

# # Find Union and Intersection of two unsorted arrays
# arr1[] = [7, 1, 5, 2, 3, 6]
# arr2[] = [3, 8, 6, 20, 7]

# union = 
# intersection = 

def find_union(arr1, arr2):
    memo = {}
            
    for i in range(0, len(arr1)):
        memo[arr1[i]] = i
        
    for i in range(0, len(arr2)):
        memo[arr2[i]] = i
                
    print(sorted(list(memo.keys())))

arr1 = [7, 1, 5, 2, 3, 6]
arr2 = [3, 8, 6, 20, 7]    
find_union(arr1, arr2)

def find_intersection(arr1, arr2):
    memo = {}
    res = []
   
    for i in range(0, len(arr1)):
        memo[arr1[i]] = i
        
    for i in range(0, len(arr2)):
        if arr2[i] in memo:
            res.append(arr2[i])
                
    print(res)

arr1 = [7, 1, 5, 2, 3, 6]
arr2 = [3, 8, 6, 20, 7]    
find_intersection(arr1, arr2)