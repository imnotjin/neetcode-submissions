# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def count(node: TreeNode, maxSoFar: int) -> None:
            if not node: 
                return 0

            res = 1 if node.val >= maxSoFar else 0
            maxSoFar = max(maxSoFar, node.val)
            res += count(node.left, maxSoFar)
            res += count(node.right, maxSoFar)
            return res

        return count(root, root.val)
