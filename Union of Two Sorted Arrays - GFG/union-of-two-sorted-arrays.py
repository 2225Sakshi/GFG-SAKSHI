#User function Template for python3

class Solution:
    
    #Function to return a list containing the union of the two arrays.
    def findUnion(self,a,b,n,m):
        n = len(a)
        m = len(b)
        i = 0
        j = 0
        union = []
        while i < n and j < m:
            if a[i] < b[j]:
                if not union or a[i] != union[-1]:
                    union.append(a[i])
                i += 1
            elif b[j] < a[i]:
                if not union or b[j] != union[-1]:
                    union.append(b[j])
                j += 1
            else:
                if not union or a[i] != union[-1]:
                    union.append(a[i])
                i += 1
                j += 1
        while i < n:
            if not union or a[i] != union[-1]:
                union.append(a[i])
            i += 1
        while j < m:
            if not union or b[j] != union[-1]:
                union.append(b[j])
            j += 1
        return union
        
        
        # return sorted(set(a+b))
        
        
        # s = set(a)
        # s.update(b)
        # union = list(s)
        # return union
        
    '''
        :param a: given sorted array a
        :param n: size of sorted array a
        :param b: given sorted array b
        :param m: size of sorted array b
        :return:  The union of both arrays as a list
        '''
        # code here 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

# Contributed by : Nagendra Jha
# Modified by : Sagar Gupta


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,m = map(int,input().strip().split())
        a = list(map(int,input().strip().split()))
        b = list(map(int,input().strip().split()))
        ob=Solution()
        li = ob.findUnion(a,b,n,m)
        for val in li:
            print(val, end = ' ')
        print()
# } Driver Code Ends