"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if node is None:
            return None

        old_to_new = {}
        old_to_new[node] = Node(val=node.val)
        q = deque([node])

        while q:
            n = q.popleft()
            for neighbor in n.neighbors:
                if neighbor not in old_to_new:
                    old_to_new[neighbor] = Node(neighbor.val)
                    q.append(neighbor)
                old_to_new[n].neighbors.append(old_to_new[neighbor])

        return old_to_new[node]
