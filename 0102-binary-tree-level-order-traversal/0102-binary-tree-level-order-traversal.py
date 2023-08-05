# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        bfs =[]
        if root is None:
            return bfs
        queue = deque([])
        queue.append(root)
        while len(queue) != 0:
            level_size = len(queue)
            curr_level =[]
            for i in range(level_size):
                curr = queue.popleft()
                curr_level.append(curr.val)
                if curr.left is not None:
                    queue.append(curr.left)
                if curr.right is not None:
                    queue.append(curr.right)
            bfs.append(curr_level)
        return bfs
            

