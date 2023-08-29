# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:  
        if root == None:
            return 0
        
        leftCount = self.countNodes(root.left)
        rightCount = self.countNodes(root.right)
        totalNode = leftCount+rightCount+1
        return totalNode        
        
        