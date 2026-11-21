# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        res = dummy = ListNode(-1)
        heap = []
        for l in lists:
            while l:
                heapq.heappush(heap, l.val)
                l = l.next
        while heap:
            dummy.next = ListNode(heapq.heappop(heap))
            dummy = dummy.next
        return res.next
