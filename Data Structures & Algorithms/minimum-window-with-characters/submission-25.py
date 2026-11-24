class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        t_count = Counter(t)
        s_count = {}
        l, r = 0, 0
        formed = 0
        n = float('inf')
        best = None

        while r < len(s):
            while r < len(s) and formed != len(t_count):
                s_count[s[r]] = s_count.get(s[r], 0) + 1
                if s[r] in t_count and s_count[s[r]] == t_count[s[r]]: 
                    formed += 1
                r += 1

            while l < r and formed == len(t_count):
                if r - l < n:
                    n = r - l
                    best = (l, r)

                s_count[s[l]] = s_count.get(s[l]) - 1
                if s[l] in t_count and s_count[s[l]] < t_count[s[l]]: 
                    formed -= 1
                l += 1

        return s[best[0]: best[1]] if best else ""
