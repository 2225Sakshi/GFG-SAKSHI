#User function Template for python3

class Solution:
    
    #Function to find the first non-repeating character in a string.
    def nonrepeatingCharacter(self,s):
        char_count = {}
        # Count occurrences of each character
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
    
        # Find the first non-repeating character
        for char in s:
            if char_count[char] == 1:
                return char
    
        # If no non-repeating character is found, return '$'
        return '$'
            
        # # for i in s:
        # #     if(s.find(i, (s.find(i)+1))) == -1:
        # #         return(i)
        # #     return '$'
        # d={}
        # for i in (s):
        #     c = s.count(i)
        #     if c==1:
        #         return i
        #     return '$'
            
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s=str(input())
        obj = Solution()
        ans=obj.nonrepeatingCharacter(s)
        if(ans!='$'):
            print(ans)
        else:
            print(-1)
            
# } Driver Code Ends