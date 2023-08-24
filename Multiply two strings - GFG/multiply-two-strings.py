#User function Template for python3


class Solution:
    def multiplyStrings(self, s1, s2):
        num1 = int(s1)
        num2 = int(s2)
        result = num1 * num2
        return str(result)
        # result = 0  # Initialize the result
        
        # for i in range(len(s1)):
        #     for j in range(len(s2)):
        #         # Convert characters to integers and multiply
        #         temp = int(s1[i]) * int(s2[j])
                
        #         # Add the product to the result
        #         result += temp
        
        # return str(result)
        # return the product string


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        a,b=input().split()
        print(Solution().multiplyStrings( a.strip() , b.strip() ))

# } Driver Code Ends