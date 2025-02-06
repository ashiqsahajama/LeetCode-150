# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        s = 0
        def dfs(node,val,res):
            if not node:
                return 0
            val += str(node.val)

            if not node.left and not node.right:
                res += int(val)
                return res
            
            return (dfs(node.left,val,res) + dfs(node.right,val,res))
        return (dfs(root,"",0))
        
        
