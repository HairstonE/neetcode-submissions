class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        BLACK, WHITE, GREY = 2, 0, 1
        adj = defaultdict(list)
        for u, v in prerequisites:
            adj[u].append(v)

        courses = [WHITE] * numCourses
        schedule = []

        def dfs(c: int) -> bool:
            if courses[c] == GREY:
                return False
            if courses[c] == BLACK:
                return True

            courses[c] = GREY
            for i in adj[c]:
                if not dfs(i):
                    return False
                

            courses[c] = BLACK
            schedule.append(c)
            return True
            
        
        for c in range(numCourses):
            if not dfs(c):
                return []

        return schedule