# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from heapq import heapify, heappop, heappush
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        for i, node in enumerate(lists):
            if node:
                min_heap.append((node.val, i, node))
        heapify(min_heap)
        res = []
        
        dummy = ListNode()
        curr = dummy

        counter = len(lists)

        while min_heap:
            val, i, node = heappop(min_heap)
            
            curr.next = node
            curr = curr.next

            if node.next:
                heappush(min_heap, (node.next.val, counter, node.next))
                counter += 1
                
        return dummy.next
