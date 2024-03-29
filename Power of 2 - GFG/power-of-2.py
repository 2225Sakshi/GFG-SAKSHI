#User function Template for python3

class Solution:
    ##Complete this function
    # Function to check if given number n is a power of two.
    def isPowerofTwo(self,n):
        if n <= 0:
            return False
    
    # Bitwise operation to check if there is only one '1' bit in n
        return (n & (n - 1)) == 0
        # if n<=0:
        #     return False
        # while (n>1):
        #     if n%2!=0:
        #         return False
        #         n=n//2
        # return True
        ##Your code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        ob=Solution()
        if ob.isPowerofTwo(n):
            print("YES")
        else:
            print("NO")
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends