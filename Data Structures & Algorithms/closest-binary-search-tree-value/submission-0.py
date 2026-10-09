# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        if not root: return -1

        def traverse(node: Optional[TreeNode], closest):
            if not node: return closest

            if abs(node.val - target) < abs(closest - target): 
                closest = node.val
            
            if target > node.val:
                return traverse(node.right, closest)
            else:
                return traverse(node.left, closest)
            

        return traverse(root, float("inf"))

        