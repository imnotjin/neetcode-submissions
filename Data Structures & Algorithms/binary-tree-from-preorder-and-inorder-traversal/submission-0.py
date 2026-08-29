# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #     1
        # 2       3
        #             4
        # 
        # preorder = 1 2 3 4
        # inorder = 2 1 3 4

        inorder_map = {}
        for i, val in enumerate(inorder):
            inorder_map[val] = i
        preorder_i = 0

        def helper(l, r):
            nonlocal preorder_i
            if l > r:
                return
            root_val = preorder[preorder_i]
            root = TreeNode(root_val)
            preorder_i += 1
            
            mid = inorder_map[root_val]

            root.left = helper(l, mid - 1)
            root.right = helper(mid + 1, r)
            return root
        
        return helper(0, len(inorder) - 1)
