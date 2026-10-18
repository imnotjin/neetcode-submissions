# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = [(node.val, i, node) for i, node in enumerate(lists) if node]
        heapq.heapify(min_heap)

        dummy = ListNode()
        curr = dummy
        counter = len(lists)

        while min_heap:
            val, i, node = heapq.heappop(min_heap)
            curr.next = node
            curr = curr.next

            if node.next:
                heapq.heappush(min_heap, (node.next.val, counter, node.next))
                counter += 1

        
        return dummy.next

            