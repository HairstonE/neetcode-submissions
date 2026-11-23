# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = [0]

        def traverse(node: Optional[TreeNode], counter):
            if not node:
                return counter
            
            counter = traverse(node.left, counter) + 1
            
            if counter == k:
                res[0] = node.val
            # counter += 1
            counter = traverse(node.right, counter)
            return counter

        traverse(root, 0)
        return res[0]
