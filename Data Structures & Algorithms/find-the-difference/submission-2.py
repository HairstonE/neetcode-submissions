class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_set = Counter(s)

        for c in t:
            if c in s_set:
                s_set[c] -= 1
                if s_set[c] == 0:
                    del s_set[c]
            else:
                return c

        return ""