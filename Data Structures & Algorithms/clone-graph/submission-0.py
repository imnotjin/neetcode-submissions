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

        def dfs(head):
            if not head:
                return
            if head in cloned:
                return cloned[head]

            new_head = Node(head.val, [])
            cloned[head] = new_head

            for neighbor in head.neighbors:
                cloned_neighbor = dfs(neighbor)
                new_head.neighbors.append(cloned_neighbor)

            return new_head
        
        return dfs(node)
        