# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        stack = []
        if root is None:
            return 0
        print(root)
        stack.append(root)
        count = 0
        while len(stack) > 0:
            n = stack.pop()
            
            count += 1
            if n.left != None:
                stack.append(n.left)
            if n.right != None:
                stack.append(n.right)
        return count