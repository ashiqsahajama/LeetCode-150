# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        prev = None
        res = float('inf')
        def inorder(node):
            if not node:
                return 
            inorder(node.left)
            nonlocal prev,res
            if prev:
                res = min(res,node.val-prev.val)
            prev = node
            inorder(node.right)
            return res
        return inorder(root)
