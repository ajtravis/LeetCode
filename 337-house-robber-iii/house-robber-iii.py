# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        rob, skip = self.dfs(root)

        return max(rob, skip)
        
    def dfs(self, root):
        if root is None:
            return (0, 0)

        left_rob, left_skip = self.dfs(root.left)
        right_rob, right_skip = self.dfs(root.right)

        rob = root.val + left_skip + right_skip
        skip = max(left_rob, left_skip) + max(right_rob, right_skip)

        return (rob, skip)