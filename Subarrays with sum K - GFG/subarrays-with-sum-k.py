#User function Template for python3
from collections import defaultdict
class Solution:
    def findSubArraySum(self, Arr, N, k):
        #optimal solution 
        
        N = len(Arr)
        preSum = 0
        count = 0
        mpp = defaultdict(int)
        mpp[0] = 1 #Setting 0 in the mpp
        for i in range(N):
            preSum+=Arr[i] #add curr element to prefix Sum
            remove = preSum - k #Calculate x-k
            count += mpp[remove]#add the number of subaar to be removed
            mpp[preSum] +=1 #update the cnt of prefix sum in the map
            
        return count
        
        
        
        # #BETTER OR BRUTE
        # N = len(Arr)  # size of the given array.
        # cnt = 0  # Number of subarrays.
    
        # for i in range(N):  # starting index i.
        #     subarray_sum = 0
        #     for j in range(i, N):  # ending index j.
        #         # calculate the sum of subarray [i...j]
        #         # sum of [i..j-1] + arr[j]
        #         subarray_sum += Arr[j]
    
        #         # Increase the count if sum == k.
        #         if subarray_sum == k:
        #             cnt += 1
    
        # return cnt
        
        
        
        # count = 0
        # for i in range(N):
        #     sum = 0
        # for j in range(N):
        #     sum+=Arr[j]
        # if (sum==k):
        #     count+=1
        # return count
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        N = int(input())
        Arr = input().split()
        for itr in range(N):
            Arr[itr] = int(Arr[itr])
        k = int(input())
        ob = Solution()
        print(ob.findSubArraySum(Arr, N, k))
# } Driver Code Ends