#Initial Template for Python 3
class Solution:
	def ZigZagMaxLength(self, nums):
	    n = len(nums)
        if n <= 1:
            return n
        max_up = max_down = 1
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                max_up = max(max_up, max_down + 1)
            elif nums[i] < nums[i-1]:
                max_down = max(max_down, max_up + 1)
        return max(max_up, max_down)
	   # n = len(nums)
    #     up = [1] * n
    #     down = [1] * n
    #     for i in range(1, n):
    #         for j in range(i):
    #             if nums[j] < nums[i]:
    #                 up[i] = max(up[i], down[j] + 1)
    #             elif nums[j] > nums[i]:
    #                 down[i] = max(down[i], up[j] + 1)
    #     return max(up[-1], down[-1])
		# Code here
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        A = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.ZigZagMaxLength(A))
# } Driver Code Ends