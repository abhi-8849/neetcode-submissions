# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dia = 0
    
        def height(node: TreeNode | None):
            if not node:
                return 0

            lefth = height(node.left)
            righth = height(node.right)
            self.dia = max(self.dia, lefth + righth)
            return 1 + max(lefth, righth)

        height(root)
        return self.dia