class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not edges:
            return n == 1
        adj = defaultdict(list)
        
        for k,v in edges:
            adj[k].append(v)
            adj[v].append(k)
        
        seen = set()

        stack = [(edges[0][0], -1)] # first node given
        seen.add(edges[0][0])

        while stack:
            node, parent = stack.pop()
            for neighbor in adj[node]:
                if neighbor == parent:
                    continue
                if neighbor not in seen:
                    seen.add(neighbor)
                    stack.append((neighbor, node))
                else:
                    return False # cycle detected(?)
        
        return len(seen) == n
