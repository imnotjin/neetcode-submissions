# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(l, node, r):
            if not node:
                return True
            
            if not (l < node.val < r):
                return False

            left = dfs(l, node.left, node.val)
            right = dfs(node.val, node.right, r)

            return left and right

        return dfs(float('-inf'), root, float('inf'))
