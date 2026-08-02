# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, root):
        result = []

        def helper(node):
            if node is None:
                return
            result.append(node.val)
            helper(node.left)
            helper(node.right)

        helper(root)
        return result

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        list1 = self.dfs(root)
        list1.sort()
        return list1[k - 1]

        
        