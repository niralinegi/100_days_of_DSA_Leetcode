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
        
