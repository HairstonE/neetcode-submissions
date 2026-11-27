class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()
        res = [0]

        def traverse(n):
            q = deque([n])

            while q:
                i = q.popleft()

                for neigh in adj[i]:
                    if neigh not in visited:
                        visited.add(neigh)
                        q.append(neigh)

            res[0] += 1

        for a in adj:
            if a not in visited:
                visited.add(a)
                traverse(a)
        if len(visited) < n:
            res[0] += (n - len(visited))
        return res[0] 
        # this can be don't with Union find.
