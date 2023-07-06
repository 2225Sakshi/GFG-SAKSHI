class Solution:
    def quickSort(self, arr, low, high):
        if low < high:
            pivot = self.partition(arr, low, high)

            self.quickSort(arr, low, pivot - 1)
            self.quickSort(arr, pivot + 1, high)

    def partition(self, arr, low, high):
        pivot = arr[low]
        i = low + 1  # Fixed: i should start from low + 1
        j = high

        while i <= j:
            while i <= j and arr[i] <= pivot:  # Fixed: Corrected the conditions in while loops
                i += 1
            while i <= j and arr[j] > pivot:  # Fixed: Corrected the conditions in while loops
                j -= 1

            if i < j:
                arr[i], arr[j] = arr[j], arr[i]

        arr[low], arr[j] = arr[j], arr[low]  # Fixed: Swapping pivot with arr[j] instead of arr[i]

        return j
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        Solution().quickSort(arr,0,n-1)
        for i in range(n):
            print(arr[i],end=" ")
        print()

# } Driver Code Ends