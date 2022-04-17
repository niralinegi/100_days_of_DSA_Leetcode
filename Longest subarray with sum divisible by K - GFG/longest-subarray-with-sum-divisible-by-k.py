#User function Template for python3
class Solution:
	def longSubarrWthSumDivByK (self,arr,  n, K) : 
		#Complete the function
		ss = 0
		memo = {}
		ans = 0
		memo[ss] = -1
		
		for idx, i in enumerate(arr):
		    ss = (ss+i)%K
		    if ss in memo:
		        ans = max(ans, idx-memo[ss])
		    else:
		        memo[ss] = idx
		        
		return ans
		    


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

	for _ in range(0,int(input())):
		n, K = map(int ,input().split())
		arr = list(map(int,input().strip().split()))
		ob = Solution()
		res = ob.longSubarrWthSumDivByK(arr, n, K)
		print(res)




# } Driver Code Ends