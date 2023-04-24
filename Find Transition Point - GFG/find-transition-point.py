def transitionPoint(arr, n):
    if arr[0]==1:
        return 0
    l=0
    h=n-1
    while(l<=h):
        mid=(l+h)//2
        if arr[mid]==1 and arr[mid-1]==0:
            return mid
        elif(arr[mid]==0):
            l=mid+1
        else:
            h=mid-1
    return -1
        
    # low=0
    # high=n-1
    # while(low<=high):
    #     mid=(low+high)/2
    #     if arr[mid]==0:
    #         low=(mid+1)
    #     else if (arr[mid]==1)
    
    
    
    # for i in range (len(arr)):
    #     if (1 in arr):
    #         return arr.index(1)
    #     return -1
    #Code here




#{ 
 # Driver Code Starts
#driver code
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(transitionPoint(arr, n))

# } Driver Code Ends