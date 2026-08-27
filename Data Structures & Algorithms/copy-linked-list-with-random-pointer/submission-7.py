"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
def print_LL(node):
    while node:
        print(f"(val: {node.val}| random: {node.random.val if node.random else None})", end="->")
        node = node.next
    print("None")
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # print_LL(head)
        if not head: return None
        node = head
        old_to_new = dict()
        # key: old node, value: new construct with same value
        # on second iter fill in random point

        while node:
            old_to_new[node] = Node(node.val, None, None)
            node = node.next

        node = head
        # print(old_to_new)
        while node:
            new_node = old_to_new[node]
            new_node.next = old_to_new[node.next] if node.next else None
            new_node.random = old_to_new[node.random] if node.random else None
            node = node.next
        
        return old_to_new[head]
            


        