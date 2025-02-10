# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = deque([root])
        r = []
        while q:
            c = 0
            a = 0
            for _ in range(len(q)):
                n = q.popleft()
                a += n.val
                c+=1
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
            r.append(a/c)
        return r


        
