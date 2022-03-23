#User function Template for python3

class Solution:
    def cutRod(self, price, n):
        # dp = [[-1 for row in range(len(price))]for col in range(n)]
        memo = {}
        return self.maxProfit(0, price, n, memo)
        
    def maxProfit(self, currentIndex, price, n, memo):
        if currentIndex >= len(price):
            return 0
            
        if n == 0:
            return 0
            
        consider = 0
        
        currentIndexLength = currentIndex + 1
        
        key = (currentIndex, n)
        if key in memo:
            return memo[key]
        
        if currentIndexLength <= n:
            consider = price[currentIndex] + self.maxProfit(currentIndex, price, n-currentIndexLength, memo)
        
        notConsider = self.maxProfit(currentIndex+1, price, n, memo)
        
        memo[key] = max(consider, notConsider)
        return memo[key]

#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.cutRod(a, n))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends