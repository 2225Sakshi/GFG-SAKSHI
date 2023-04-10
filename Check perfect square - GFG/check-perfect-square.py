#User function Template for python3

#User function Template for python3
class Solution:
    def isPerfectSquare (self, n):
       import math
       sq = math.sqrt(n)
       if int(sq)*int(sq) == n:
           return 1
       else:
           return 0
        # code here 


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        
        ob = Solution()
        print(ob.isPerfectSquare(n))
# } Driver Code Ends