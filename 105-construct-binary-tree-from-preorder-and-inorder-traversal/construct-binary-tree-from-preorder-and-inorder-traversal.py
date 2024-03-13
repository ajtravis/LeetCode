# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        stack = []
        inorder_ind = 0
        root = TreeNode(preorder[0])
        stack.append(root)
        curr = root
        right = False
        for elem in preorder[1:]:
            node = TreeNode(elem)
            while stack and inorder[inorder_ind] == stack[-1].val:
                inorder_ind += 1
                curr = stack.pop() 
                right = True
            stack.append(node)
            if right:
                curr.right = node
            else:
                curr.left = node
            curr = node
            right = False
        return root