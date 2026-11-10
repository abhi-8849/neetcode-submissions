# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True
        def height(node):
            if not node:
                return 0

            lefth = height(node.left)
            righth = height(node.right)

            if abs(lefth - righth) > 1:
                self.balanced = False

            return 1 + max(lefth, righth)
        
        height(root)
        return self.balanced
        