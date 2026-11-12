# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def isValid(node: Optional[Treenode], low: int, high: int) -> int:
            if not node:
                return True

            if not (low < node.val < high):
                return False

            leftRes = isValid(node.left, low, node.val)
            rightRes = isValid(node.right, node.val, high)
            return leftRes and rightRes
        
        return isValid(root, low = float('-inf'), high = float('inf'))