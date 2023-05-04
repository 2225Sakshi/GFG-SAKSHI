#User function Template for python3

def missingNumber( A, N):
    sum = 0
    for i in range(1, N+1):
        sum += i
    s2 = 0
    for i in range(N-1):
        s2 += A[i]
    return sum - s2
     # Your code goes here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        print(missingNumber(a, n))

        T -= 1


if __name__ == "__main__":
    main()





    
# } Driver Code Ends