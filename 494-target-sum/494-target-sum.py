class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        return self.totalWays(0, nums, target, memo)
        
    def totalWays(self, currentIndex, nums, target, memo):
        if currentIndex >= len(nums) and target == 0:
            return 1
        if currentIndex >= len(nums) and target != 0:
            return 0
        
        currentKey = (currentIndex, target)
        if currentKey in memo:
            return memo[currentKey]
        pos_sign = self.totalWays(currentIndex+1, nums, target-nums[currentIndex], memo)
        neg_sign = self.totalWays(currentIndex+1, nums, target+nums[currentIndex], memo)
        
        memo[currentKey] = pos_sign+neg_sign
        return memo[currentKey]