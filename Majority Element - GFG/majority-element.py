#User function template for Python 3

class Solution:
    def majorityElement(self, A, N):
        
        freq={}
        for i in A:
            if i not in freq:
                freq[i]=1
            else:
                freq[i]+=1
            if freq[i]>N/2:
                return i 
        return -1
        
        
        # count = 1
        # candidate = A[0]
        # for i in range(1, N):
        #     if A[i] == candidate:
        #         count += 1
        #     else:
        #         count -= 1
                
        #     if count == 0:
        #         candidate = A[i]
        #         count = 1
                
        # count = 0
        # for i in range(N):
        #     if A[i] == candidate:
        #         count += 1
                
        # if count > N/2:
        #     return candidate
        # else:
        #     return -1
        #Your code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

from sys import stdin


def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=[int(x) for x in input().strip().split()]
            
            
            obj = Solution()
            print(obj.majorityElement(A,N))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends