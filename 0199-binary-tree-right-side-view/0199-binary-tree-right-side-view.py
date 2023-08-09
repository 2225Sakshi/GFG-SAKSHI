from typing import List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if root is None:
            return result
        
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            
            for i in range(level_size):
                curr = queue.popleft()
                if i == level_size - 1:
                    result.append(curr.val)
                if curr.left is not None:
                    queue.append(curr.left)
                if curr.right is not None:
                    queue.append(curr.right)
        
        return result
from typing import List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if root is None:
            return result
        
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            
            for i in range(level_size):
                curr = queue.popleft()
                if i == level_size - 1:
                    result.append(curr.val)
                if curr.left is not None:
                    queue.append(curr.left)
                if curr.right is not None:
                    queue.append(curr.right)
        
        return result
