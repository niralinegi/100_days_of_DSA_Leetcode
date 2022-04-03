class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        memo = {}
        res = []
        for num in nums1:
            if num not in memo:
                memo[num] = True
                
        for num in nums2:
            if num in memo and memo[num] == True:
                res.append(num)
                memo[num] = False
                
        return res
        
