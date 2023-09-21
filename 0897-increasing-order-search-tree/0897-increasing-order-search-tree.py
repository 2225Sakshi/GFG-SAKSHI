# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def increasingBST(self, root: TreeNode, tail=None) -> TreeNode:
        if root is None:
            return tail
        
        # Recursively traverse the left subtree
        result = self.increasingBST(root.left, root)
        
        # Set the left subtree of the current root to None
        root.left = None
        
        # Recursively traverse the right subtree with the updated tail
        root.right = self.increasingBST(root.right, tail)
        
        return result
