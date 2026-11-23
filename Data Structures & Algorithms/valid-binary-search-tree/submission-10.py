# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node: Optional[TreeNode], lo: int, hi: int):
            if not node: return True

            if node.val < hi:
                left = dfs(node.left, lo, node.val)
            else:
                return False
            if node.val > lo:
                right = dfs(node.right, node.val, hi)
            else:
                return False
            
            return left and right


        return dfs(root.left, float('-inf'), root.val) and dfs(root.right, root.val, float('inf')) 
