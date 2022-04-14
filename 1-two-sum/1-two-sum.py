class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        
        for i, val in enumerate(nums):
            complement = target - val
            if complement in prevMap:
                return prevMap[complement], i
            else:
                prevMap[val] = i
        