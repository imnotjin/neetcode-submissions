# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # group_prev -> ...kth -> group_next
        dummy = ListNode()
        dummy.next = head
        group_prev = dummy

        while True:
            kth = group_prev
            # count k nodes
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            group_next = kth.next
            # reverse
            prev, curr = group_next, group_prev.next
            while curr != group_next:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            # connect
            old_first = group_prev.next
            group_prev.next = kth
            group_prev = old_first
