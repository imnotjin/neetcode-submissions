# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""

        res = []

        q = deque([root])

        while q:
            node = q.popleft()
        
            if node:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                res.append('#')
        
        return ','.join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        
        tokens = data.split(",")
        root = TreeNode(int(tokens[0]))
        q = deque([root])
        index = 1

        while q and index < len(tokens):
            node = q.popleft()

            if tokens[index] != '#':
                node.left = TreeNode(int(tokens[index]))
                q.append(node.left)
            index += 1

            if index < len(tokens) and tokens[index] != "#":
                node.right = TreeNode(int(tokens[index]))
                q.append(node.right)
            index += 1
        
        return root
