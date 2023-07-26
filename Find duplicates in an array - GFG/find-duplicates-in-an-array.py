class Solution:
    def duplicates(self, arr, n): 
        freq = [0] * n
        for num in arr:
            freq[num] += 1
        
        # Step 2: Find elements with count greater than 1
        duplicates_list = [i for i in range(n) if freq[i] > 1]
        
        # Step 3: Return result list in ascending order
        return sorted(duplicates_list) if duplicates_list else [-1]
        # if arr[i] == arr[i+1]:
        #     return arr.data
        # return -1
    	# code here
    	    


#{ 
 # Driver Code Starts
if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()



# } Driver Code Ends