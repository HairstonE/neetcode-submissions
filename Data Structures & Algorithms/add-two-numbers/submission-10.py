# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # add to l1, save carry on way up
        # remember left overs
        res = adder = ListNode(-1, None)
        carry = 0
        while l1 and l2:
            val = l1.val + l2.val + carry
            carry = val // 10
            adder.next = ListNode(val % 10) 
            adder = adder.next
            l1 = l1.next
            l2 = l2.next

        while l1: 
            val = l1.val  + carry
            carry = val // 10
            adder.next = ListNode(val % 10) 
            adder = adder.next
            l1 = l1.next
        while l2: 
            val = l2.val + carry
            carry = val // 10
            adder.next = ListNode(val % 10) 
            adder = adder.next
            l2 = l2.next
        if carry: 
            adder.next = ListNode(carry)

        return res.next
        