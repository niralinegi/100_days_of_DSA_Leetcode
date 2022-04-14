class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        answer = 0
        prefix_sum = 0
        memo = {}
        memo[prefix_sum] = 1
        
        for current_value in nums:
            prefix_sum += current_value
            current_rem = prefix_sum % k
            
            if current_rem in memo:
                answer += memo[current_rem]
                memo[current_rem] = memo[current_rem] + 1
            else:
                memo[current_rem] = 1
                
        return answer
    