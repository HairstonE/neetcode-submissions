class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for u, v in prerequisites:
            adj[u].append(v)

        WHITE, GREY, BLACK = 0, 1, 2
        courses = [WHITE] * numCourses
        schedule = []

        def dfs(i: int) -> bool:
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

        for c in range(numCourses):
            if not dfs(c):
                return []

        return schedule
