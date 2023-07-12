#User function Template for python3
from typing import List
class Solution:
    def nextPermutation(self, N, arr):
            n = len(arr) # size of the array.
        
            # Step 1: Find the break point:
            ind = -1 # break point
            for i in range(n-2, -1, -1):
                if arr[i] < arr[i + 1]:
                    # index i is the break point
                    ind = i
                    break
        
            # If break point does not exist:
            if ind == -1:
                # reverse the whole array:
                arr.reverse()
                return arr
        
            # Step 2: Find the next greater element
            #         and swap it with arr[ind]:
            for i in range(n - 1, ind, -1):
                if arr[i] > arr[ind]:
                    arr[i], arr[ind] = arr[ind], arr[i]
                    break
        
            # Step 3: reverse the right half:
            arr[ind+1:] = reversed(arr[ind+1:])
        
            return arr
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        ans = ob.nextPermutation(N, arr)
        for i in range(N):
            print(ans[i],end=" ")
        print()
# } Driver Code Ends