#User function Template for python3

class Solution:
    #Function to find the nth catalan number
    def findCatalan(self,n):
        #return the nth Catalan number.
        memo = {}
        return self.nthCatalan(n, memo)
        
    def nthCatalan(self, n, memo):
        
        if n == 0 or n == 1:
            return 1
            
        ways = 0
        key = n
        
        if key in memo:
            return memo[key]
            
        for i in range(0, n):
            ways += self.nthCatalan(i, memo) * self.nthCatalan(n-i-1, memo)
            
        memo[key] = ways
        return memo[key]

#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__': 
    t=int(input())
    for tcs in range(t):
        n=int(input())
        
        print(Solution().findCatalan(n))
        
# } Driver Code Ends