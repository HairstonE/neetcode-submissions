# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def print_LL(node):

    while node:
        print(node.val, end="->")
        node = node.next
    print("None")

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head: return head
        if not head.next: return None

        slow, fast = head, head
        while n > 0:
            n -= 1
            fast = fast.next
        print_LL(fast)
        if not fast: return head.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        # print_LL(slow)

        return head
        