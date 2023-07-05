# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        stack = []
        curr = root
        prev_val = float('-inf')  # Initialize the previously visited node value
        min_diff = float('inf')  # Initialize the minimum difference to positive infinity

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()

            # Calculate the difference with the previous node and update the minimum difference
            min_diff = min(min_diff, abs(curr.val - prev_val))

            prev_val = curr.val  # Update the previously visited node value
            curr = curr.right

        return min_diff
            
            