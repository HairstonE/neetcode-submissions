# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def printLL(self, node):
        s = ""
        while node:
            s += str(node.val) + "->"
            node = node.next
        
        print(s)

    def reverse(self, node) -> ListNode:
        prev = None
        while node:
            temp = node.next
            node.next = prev
            prev = node
            node = temp
        
        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next: return
        fast, slow = head, head
        slower = None
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        second = slow.next
        slow.next = None
        second = self.reverse(second)
        
        l1 = head
        l2 = second

        while l2:
            t1 = l1.next
            t2 = l2.next

            l1.next = l2
            l2.next = t1

            l1 = t1
            l2 = t2


        
