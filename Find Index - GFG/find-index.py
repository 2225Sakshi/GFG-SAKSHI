#User function Template for python3

class Solution:
    def findIndex (self,a, N, key ):
        n=[]
        for i in range(N):
            if a[i]==key:
                n.append(i)
        if len(n) == 0:
            return -1 , -1
        else:
            return n[0],n[-1]                                                  
        #code here.


#{ 
 # Driver Code Starts
#Initial Template for Python 3


t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    key=int(input())
    ob = Solution()
    ans=ob.findIndex(a, n, key )
    print(*ans)
    
# } Driver Code Ends