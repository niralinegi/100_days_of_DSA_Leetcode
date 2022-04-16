import math
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        memo = {}
        res = 0

        for i in range(0, len(answers)):
            if answers[i] in memo:
                memo[answers[i]] += 1
            else:
                memo[answers[i]] = 1
            
        for key, val in memo.items():
            res += (key+1)*math.ceil(val/(key+1))
            
        return res
            
