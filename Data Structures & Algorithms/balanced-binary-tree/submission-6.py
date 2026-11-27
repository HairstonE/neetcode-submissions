# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        def depth(node) -> (int, bool):
            if not node: 
                return (0, True)

            ld, lb = depth(node.left)
            rd, rb = depth(node.right)
            if not lb or not rb: return (-1, False)

            return (max(ld, rd) + 1, abs(ld - rd) <= 1)

        
        return depth(root)[1]