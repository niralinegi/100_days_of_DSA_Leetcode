class Solution:
    def jump(self, nums: List[int]) -> int:
        memo = {}
        return self.minWays(nums, 0, memo)
    
    def minWays(self, nums, currentIndex, memo):
        if currentIndex >= len(nums)-1:
            return 0
        
        if nums[currentIndex] == 0:
            return 10001
        
        key = currentIndex
        currentJump = nums[currentIndex]
        
        if key in memo:
            return memo[key]
        
        ans = 10001
        
        for i in range(1, currentJump+1):
            tempAns = 1 + self.minWays(nums, currentIndex+i, memo)
            ans = min(ans, tempAns)
            
        memo[key] = ans
        return memo[key]
            
        
