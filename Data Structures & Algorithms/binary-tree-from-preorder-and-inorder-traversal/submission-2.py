# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # if not preorder or not inorder:
        #     return None
        # root_val = preorder[0]
        # root = TreeNode(root_val)

        # idx = inorder.index(root_val)
        # root.left = self.buildTree(preorder[1:idx+1], inorder[:idx])
        # root.right = self.buildTree(preorder[idx+1:], inorder[idx+1:])
        # return root
        inorder_map = {val: i for i, val in enumerate(inorder)}
        p_idx = 0

        def dfs(l, r):
            nonlocal p_idx
            if l > r:
                return
            root_val = preorder[p_idx]
            root = TreeNode(root_val)
            p_idx += 1

            i_idx = inorder_map[root_val]

            root.left = dfs(l, i_idx - 1)
            root.right = dfs(i_idx + 1, r)
            return root
        
        return dfs(0, len(inorder) - 1)