#User function Template for python3

import sys
class Solution:
    
    #Function to find the minimum element in sorted and rotated array.
    def minNumber(self, arr,low,high):
        low = 0
        high = len(arr) - 1
        ans = sys.maxsize
    
        while low <= high:
            mid = (low + high) // 2
    
            # search space is already sorted
            # then arr[low] will always be
            # the minimum in that search space:
            if arr[low] <= arr[high]:
                ans = min(ans, arr[low])
                break
                
            if arr[low] <= arr[mid]:  # if left part is sorted
                ans = min(ans, arr[low])  # keep the minimum
                low = mid + 1  # eliminate left half
    
            else:  # if right part is sorted
                ans = min(ans, arr[mid])  # keep the minimum
                high = mid - 1  # eliminate right half
    
        return ans
        #Your code here


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
            print(obj.minNumber(A,0,N-1))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends