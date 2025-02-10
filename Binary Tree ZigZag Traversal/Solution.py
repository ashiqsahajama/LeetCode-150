# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        c = 0
        q = deque([root])
        res = []
        while q:
            r = []
            for _ in range(len(q)):
                n = q.popleft()
                r.append(n.val)
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
            if c%2==0:
                res.append(r)
            else:
                res.append(r[::-1])
            c+=1
        return res
        
