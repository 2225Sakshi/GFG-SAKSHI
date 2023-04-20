from typing import List


class Solution:
    def finLength(self, N : int, color : List[int], radius : List[int]) -> int:
        st1=[]
        st2=[]
        for i in range(N):
            if len(st1)==0:
                st1.append(color[i])
                st2.append(radius[i])
            else:
                if (st1[-1]==color[i]) and (st2[-1]==radius[i]):
                    st1.pop()
                    st2.pop()
                else:
                    st1.append(color[i])
                    st2.append(radius[i])
        return len(st1)
        # code here
        



#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        N = int(input())
        
        
        color=IntArray().Input(N)
        
        
        radius=IntArray().Input(N)
        
        obj = Solution()
        res = obj.finLength(N, color, radius)
        
        print(res)
        

# } Driver Code Ends