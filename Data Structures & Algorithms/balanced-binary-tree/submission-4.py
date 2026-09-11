# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalancedHelper(self, node: Optional[TreeNode], depth: int) -> list[int, bool]:
        if not node: return [depth, True]

        dl, bl = self.isBalancedHelper(node.left, depth + 1) # [2, true]
        dr, br = self.isBalancedHelper(node.right, depth + 1)
        
        if not (bl and br): return [depth, bl and br]

        return [max(dl, dr), dr - 1 <= dl <= dr+1]


    def isBalanced(self, root: Optional[TreeNode]) -> bool:
    
        return self.isBalancedHelper(root, 0)[1]

        

        