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
        
        second = slow.next
        slow.next = None
        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        # self.print_LL(head)
        # self.print_LL(prev)
        node = head
        while prev:
            tmp1, tmp2 = node.next, prev.next
            node.next = prev
            prev.next = tmp1
            node, prev = tmp1, tmp2
            

    def print_LL(self, head):
        while head:
            print(head.val, end="\t")
            head = head.next
        print()



