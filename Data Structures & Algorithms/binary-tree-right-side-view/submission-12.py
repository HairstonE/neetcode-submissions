# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def bfs(root):
            if not root: return

            q = deque([(root, 0)])

            while q:
                node, depth = q.popleft()
                if depth < len(res):
                    res[depth] = node.val
                else:
                    res.append(node.val)
                if node.left: q.append((node.left, depth + 1))
                if node.right: q.append((node.right, depth + 1))


        bfs(root)
        return res