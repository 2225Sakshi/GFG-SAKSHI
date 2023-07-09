from typing import List
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        p, n = [x for x in nums if x > 0], [x for x in nums if x < 0]
        a = []
        for i in range(len(p)):
            a.append(p[i])
            a.append(n[i])
        return a  
#         n = len(A)

#             # Define array for storing the ans separately.
#         ans = [0] * n

#             # positive elements start from 0 and negative from 1.
#         posIndex, negIndex = 0, 1
#         for i in range(n):

#                 # Fill negative elements in odd indices and inc by 2.
#             if A[i] < 0:
#                 ans[negIndex] = A[i]
#                 negIndex += 2

#                 # Fill positive elements in even indices and inc by 2.
#             else:
#                 ans[posIndex] = A[i]
#                 posIndex += 2

#         return ans