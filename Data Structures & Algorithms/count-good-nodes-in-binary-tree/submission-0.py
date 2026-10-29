# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, max_so_far):
            if not node:
                return 0

            count = 1 if node.val >= max_so_far else 0

            newMax = max(node.val, max_so_far)

            count += dfs(node.left, newMax)
            count += dfs(node.right, newMax)
            return count

        return dfs(root, root.val)