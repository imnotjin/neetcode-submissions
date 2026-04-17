# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, node, amount):
        prev = None
        curr = node
        for _ in range(amount):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        entry_node = head
        exit_node = head

        for _ in range(left - 1):
            prev_node = entry_node
            entry_node = entry_node.next

        if entry_node == head:
            prev_node = None

        for _ in range(right):
            exit_node = exit_node.next

        new_head = self.reverse(entry_node, right - left + 1)

        # print(entry_node.val)
        # print(exit_node.val)
        # print(new_head.val)

        if prev_node:
            prev_node.next = new_head
        entry_node.next = exit_node
        
        return new_head if left == 1 else head
