class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)

        for u,v in prerequisites:
            adj[u].append(v)

        WHITE, BLACK, GREY = 0, 1, 2

        courses = [0] * numCourses
        schedule = []
        def dfs(i: int):
            if courses[i] == GREY:
                return False
            if courses[i] == BLACK:
                return True

            courses[i] = GREY

            for n in adj[i]:
                if not dfs(n):
                    return False

            courses[i] = BLACK
            schedule.append(i)
            return True


        for i in range(numCourses):
            if not dfs(i):
                return []
        return schedule