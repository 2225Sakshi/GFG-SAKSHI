#User function Template for python3

class Solution:
    def getPairsCount(self, arr, n, k):
        count=0
        freq={}
        for i in arr:
            target=k-i
            if target in freq:
                count+=freq[target]
            if i not in freq:
                freq[i]=1
            else:
                freq[i]+=1
        return count
            
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getPairsCount(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends