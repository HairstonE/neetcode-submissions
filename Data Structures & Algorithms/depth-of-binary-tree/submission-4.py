# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = 0
        q = deque([(root, 0)])
        while q:
            
            
            for i in range(len(q)):
                node, lvl = q.popleft()
                res = max(res, lvl)
                if node:
                    q.append((node.left, lvl+1))
                    q.append((node.right,lvl+1))

        return res




