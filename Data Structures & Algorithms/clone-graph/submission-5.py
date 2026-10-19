"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        cloned = {}

        def dfs(node):
            if not node:
                return None
            if node.val in cloned:
                return cloned[node.val]
            clone = Node(node.val)
            cloned[node.val] = clone
            for nei in node.neighbors:
                nei_clone = dfs(nei)
                clone.neighbors.append(nei_clone)
            return clone        
        return dfs(node)

