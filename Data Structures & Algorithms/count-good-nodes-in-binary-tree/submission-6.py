# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node: TreeNode, maxSoFar: int) -> int:
            if not node:
                return 0

            count = 1 if node.val >= maxSoFar else 0
            newMax = max(node.val, maxSoFar)

            if node.left:
                count += dfs(node.left, newMax)
            if node.right:
                count += dfs(node.right, newMax)

            return count
        
        return dfs(root, root.val)