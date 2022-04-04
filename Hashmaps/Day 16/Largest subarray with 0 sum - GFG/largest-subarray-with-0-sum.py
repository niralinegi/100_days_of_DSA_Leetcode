#Your task is to complete this function
#Your should return the required output
class Solution:
    def maxLen(self, n, arr):
        #Code here
        
        memo = {}
        prefixSum = 0
        answer = 0
        
        memo[prefixSum] = -1
        
        for i in range(0,n):
            prefixSum += arr[i]
            if prefixSum in memo:
                answer = max(answer, i - memo[prefixSum])
            else:
                memo[prefixSum] = i
                
        return answer

#{ 
#  Driver Code Starts
if __name__=='__main__':
    t= int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxLen(n ,arr))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends
