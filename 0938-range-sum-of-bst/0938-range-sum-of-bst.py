# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        sum = 0
        # def inRange(num):
        #     if low <= num.val and high >= num.val:
        #         return True
        #     else:
        #         return False
        stack = [root] 
        while len(stack) > 0:
            cur = stack.pop(-1)
            if cur.val >= low and cur.val <= high:
                sum += cur.val
            left = cur.left
            right = cur.right
            if left != None:
                stack.append(left)
            if right != None:
                stack.append(right)
        return sum