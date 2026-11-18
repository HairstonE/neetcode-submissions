class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)

        for u,v in prerequisites:
            adj[u].append(v)
        BLACK, GREY, WHITE = 0, 1, 2
        courses = [WHITE] * numCourses
        def dfs(c: int) -> bool:
            if courses[c] == GREY:
                return False
            if courses[c] == BLACK:
                return True

            courses[c] = GREY

            for n in adj[c]:
                if not dfs(n):
                    return False
            
            courses[c] = BLACK
            return True


            

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True
