#User function Template for python3

class Solution:
	def pushZerosToEnd(self,arr, n):
	    j=-1
	    for i in range(0,n):
	        if (arr[i]!=0):
	            j+=1
	            arr[j], arr[i] = arr[i], arr[j]
	   ## n = len(arr)
    #     temp = ()
    #     k = 0
    #     for i in arr:
    #         if i != 0:
    #             temp.append[i]
    #     for i in range(k):
    #         temp.append(0)
    #     for i in range(n):
    #         arr[i]=temp[i]
        

    	# code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.pushZerosToEnd(arr, n)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1
# } Driver Code Ends