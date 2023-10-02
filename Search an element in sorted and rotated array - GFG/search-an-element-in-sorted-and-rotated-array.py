#User function Template for python3

def Search(arr,n,k):
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2

        # if mid points the target
        if arr[mid] == k:
            return mid

        # if left part is sorted
        if arr[low] <= arr[mid]:
            if arr[low] <= k and k <= arr[mid]:
                # element exists
                high = mid - 1
            else:
                # element does not exist
                low = mid + 1
        else:  # if right part is sorted
            if arr[mid] <= k and k <= arr[high]:
                # element exists
                low = mid + 1
            else:
                # element does not exist
                high = mid - 1
    return -1
    #code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tcs=int(input())
    for _ in range(tcs):
        n=int(input())
        arr=[int(x) for x in input().split()]
        k=int(input())

        print(Search(arr,n,k))

# } Driver Code Ends