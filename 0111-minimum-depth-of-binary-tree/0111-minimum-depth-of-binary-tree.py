# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        min_dep = 0
        queue = deque([root])
        
        while queue:
            min_dep += 1
            level_size = len(queue)
            
            for i in range(level_size):
                curr = queue.popleft()
                if curr.left is None and curr.right is None:
                    return min_dep
                if curr.left is not None:
                    queue.append(curr.left)
                if curr.right is not None:
                    queue.append(curr.right)
        
        return min_dep
