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

        def dfs(node_to_clone):
            if not node_to_clone:
                return
            if node_to_clone in cloned:
                return cloned[node_to_clone]

            cloned_node = Node(node_to_clone.val, [])
            cloned[node_to_clone] = cloned_node

            for neighbor in node_to_clone.neighbors:
                cloned_neighbor = dfs(neighbor)
                cloned_node.neighbors.append(cloned_neighbor)

            return cloned_node
        
        return dfs(node)
        