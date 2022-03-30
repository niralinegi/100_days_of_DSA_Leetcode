class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        memo = {}
        return self.lengthOfLCS(s, s[::-1], 0, 0, len(s), len(s[::-1]), memo)
    
    def lengthOfLCS(self, s1, s2, i, j, m, n, memo):
        if i >= m or j >= n:
            return 0
        

        ans = 0
        key = (i, j)
        
        if key in memo:
            return memo[key]
        
        if s1[i] == s2[j]:
            ans = 1 + self.lengthOfLCS(s1, s2, i+1, j+1, m, n, memo)
            
        else:
            a = self.lengthOfLCS(s1, s2, i+1, j, m, n, memo)
            b = self.lengthOfLCS(s1, s2, i, j+1, m, n, memo)
            ans = max(a, b)
            
        memo[key] = ans
        return memo[key]
            
        
    
    
        