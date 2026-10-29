# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # split and disconnect
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        head_two = slow.next
        slow.next = None

        # reverse head_two
        prev, curr = None, head_two
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        head_two = prev

        # merge
        dummy = ListNode()
        dummy.next = head
        tail = dummy
        while head_two:
            tail.next = head
            head = head.next
            tail = tail.next

            tail.next = head_two
            head_two = head_two.next
            tail = tail.next
        tail.next = head


