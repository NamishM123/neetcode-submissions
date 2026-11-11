class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def helper(root):
            if root is None:
                return 0

            left = helper(root.left)
            right = helper(root.right)

            # Longest path passing through this node
            self.diameter = max(self.diameter, left + right)

            # Return this subtree's height to its parent
            return 1 + max(left, right)

        helper(root)

        return self.diameter