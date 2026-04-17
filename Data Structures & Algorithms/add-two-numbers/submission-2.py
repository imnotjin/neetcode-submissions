# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum1 = self.numberfy(l1)
        sum2 = self.numberfy(l2)

        total = sum1 + sum2

        print(total)
        ans = self.nodify(total)

        return ans
    
    def numberfy(self, head):
        number = 0
        digit = 1
        while head:
            number += head.val * digit
            digit *= 10
            head = head.next
        return number

    def nodify(self, number):
        if number == 0:
            return ListNode(0)
        
        dummy = ListNode()
        curr = dummy

        while number > 0:
            digit = number % 10
            curr.next = ListNode(digit)
            curr = curr.next
            number //= 10
        
        return dummy.next
            
