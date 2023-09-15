# User function Template for Python3

class Solution:
    def equalPartition(self, N, arr):
        # Calculate the sum of all elements in the array
        total_sum = sum(arr)
        
        # If the total sum is odd, it's not possible to divide into equal partitions
        if total_sum % 2 != 0:
            return 0
        
        # Initialize a list dp to represent whether a sum is achievable
        dp = [0] * (total_sum + 1)
        dp[0] = 1
        
        # Iterate through the elements in the array
        for i in range(N):
            for j in range(total_sum, arr[i] - 1, -1):
                dp[j] = dp[j] or dp[j - arr[i]]
        
        # If dp[total_sum//2] is 1, it's possible to divide into equal partitions
        return dp[total_sum // 2]
            # code here


#{ 
 # Driver Code Starts
# Initial Template for Python3

import sys
input = sys.stdin.readline
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for it in range(N):
            arr[it] = int(arr[it])
        
        ob = Solution()
        if (ob.equalPartition(N, arr) == 1):
            print("YES")
        else:
            print("NO")
# } Driver Code Ends