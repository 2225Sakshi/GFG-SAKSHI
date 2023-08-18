class Solution:
    #Back-end complete function Template for Python 3
    
    #Function to find the leaders in the array.
    #brute force
    def leaders(self, A, N):
        lis = []
        max_elem = A[N - 1]  # Initialize the maximum element as the last element of the array
    
        # Start checking from the end whether a number is greater
        # than the max number from the right, hence a leader.
        for i in range(N - 1, -1, -1):
            if A[i] >= max_elem:
                max_elem = A[i]
                lis.append(max_elem)
                
    
        lis.reverse()
        return lis

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


    
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        N=int(input())
        
        A=[int(x) for x in input().strip().split()]
        obj = Solution()
        
        A=obj.leaders(A,N)
        
        for i in A:
            print(i,end=" ")
        print()
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends