"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cloned = {None: None}
        cur = head
        while cur:
            copy = Node(cur.val)
            cloned[cur] = copy
            cur = cur.next
        
        cur = head
        while cur:
            copy = cloned[cur]
            copy.next = cloned[cur.next]
            copy.random = cloned[cur.random]
            cur = cur.next
        
        return cloned[head]
        