#User function Template for python3

class Solution:
    def lenOfLongSubarr (self, arr, n, k) : 
        sum_indices = {0: -1}
        s = 0
        max_len = 0
        for i in range(n):
            s += arr[i]
            if s - k in sum_indices:
                max_len = max(max_len, i - sum_indices[s-k])
            if s not in sum_indices:
                sum_indices[s] = i
        return max_len
        
        
        # max_len = 0
        # for i in range(n):
        #     s = 0
        #     for j in range(i, n):
        #         s += arr[j]
        #         if s == k:
        #             max_len = max(max_len, j-i+1)
        # return max_len
                
        #Complete the function
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    
    n, k = map(int , input().split())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    print(ob.lenOfLongSubarr(arr, n, k))




# } Driver Code Ends