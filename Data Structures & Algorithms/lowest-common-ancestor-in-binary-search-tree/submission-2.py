# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        if p.val > q.val:
            p, q = q, p

        def search(node: Optional[TreeNode]) -> Optional[TreeNode]:
            if not node:
                return

            if p.val <= node.val and q.val >= node.val:
                return node

            if p.val < node.val and q.val < node.val:
                return search(node.left)
            else:
                return search(node.right)

        return search(root)
