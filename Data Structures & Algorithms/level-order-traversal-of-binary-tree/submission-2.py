# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
 
        def bfs(node: Optional[TreeNode]):
            if not node: return

            q = deque([node])

            while q:
                level = []
                for _ in range(len(q)):
                    n = q.popleft()

                    level.append(n.val)
                    if n.left:
                        q.append(n.left)
                    if n.right:
                        q.append(n.right)
                res.append(level[:])

        bfs(root)
        return res