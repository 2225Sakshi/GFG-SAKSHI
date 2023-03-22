#User function Template for python3
from collections import Counter
class Solution:
    def firstElement(self, arr, n, k): 
        c=Counter(arr)
        for i in arr:
            if c[i]==k:
                return i 
        return -1




#{ 
 # Driver Code Starts
#Initial Template for Python 3




t=int(input())
for _ in range(0,t):
    n,k=list(map(int,input().split()))
    a=list(map(int,input().split()))
    ob=Solution()
    print(ob.firstElement(a,n,k))








# } Driver Code Ends