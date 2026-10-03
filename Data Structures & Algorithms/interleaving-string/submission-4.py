class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        memo = {}

        def dfs(i: int, j: int, k: int) -> bool:
            if (i,j) in memo: return memo[(i,j)]
            if k >= len(s3):
                return True
            if i >= len(s1) and j >= len(s2):
                return False

            res = False
            if i < len(s1) and s3[k] == s1[i]:
                res |= dfs(i + 1, j, k + 1)
            if j < len(s2) and s3[k] == s2[j]:
                res |= dfs(i, j + 1, k + 1)

            memo[(i, j)] = res
            return res

        if Counter(s1) + Counter(s2) != Counter(s3):
            return False

        return dfs(0, 0, 0)
