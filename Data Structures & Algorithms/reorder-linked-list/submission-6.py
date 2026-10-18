# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow
        second = mid.next
        mid.next = None

        prev, curr = None, second
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        second_head = prev

        dummy = ListNode()
        tail = dummy
        while head or second_head:
            if head:
                tail.next = head
                head = head.next
                tail = tail.next
            if second_head:
                tail.next = second_head
                second_head = second_head.next
                tail = tail.next

