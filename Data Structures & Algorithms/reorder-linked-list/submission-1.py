# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodes = []
        while head:
            nodes.append(head)
            head = head.next
        
        dummy = ListNode()
        curr = dummy
        l, r = 0, len(nodes) - 1

        while l < r:
            curr.next = nodes[l]
            l += 1
            curr = curr.next

            curr.next = nodes[r]
            r -= 1
            curr = curr.next
        
        if len(nodes) % 2 != 0:
            curr.next = nodes[r]
            curr = curr.next
        curr.next = None
            
            