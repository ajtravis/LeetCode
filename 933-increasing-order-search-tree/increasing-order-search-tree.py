class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root

        inorderArr = []

        def _inorder(root):
            if root is None:
                return 

            _inorder(root.left)
            inorderArr.append(root.val)
            _inorder(root.right)

        def _buildTree(inorderArr):
            root = TreeNode(inorderArr[0])
            initialRoot = root

            for indx in range(1, len(inorderArr)):
                newNode = TreeNode(inorderArr[indx])

                root.left = None
                root.right = newNode
                root = root.right

            return initialRoot

        _inorder(root)
        result = _buildTree(inorderArr)

        return result