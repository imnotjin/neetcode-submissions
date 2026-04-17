# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0
        def recurse(node, prev):
            nonlocal ans
            if not node:
                return
            if node.val >= prev:
                ans += 1
            recurse(node.left, max(prev, node.val))
            recurse(node.right, max(prev, node.val))
        recurse(root, root.val)
        return ans
