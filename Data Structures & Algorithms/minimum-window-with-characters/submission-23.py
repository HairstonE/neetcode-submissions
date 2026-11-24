class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        t_count = Counter(t)
        s_count = {}
        l, r = 0, 0
        formed = 0
        res = None

        while r < len(s):
            while r < len(s) and formed != len(t_count):
                s_count[s[r]] = s_count.get(s[r], 0) + 1
                if s[r] in t_count and s_count[s[r]] == t_count[s[r]]: 
                    formed += 1
                r += 1

            while l < r and formed == len(t_count):
                if not res:
                    res = s[l:r]
                else:
                    res = min(res, s[l:r], key=lambda x: len(x))

                s_count[s[l]] = s_count.get(s[l]) - 1
                if s[l] in t_count and s_count[s[l]] < t_count[s[l]]: 
                    formed -= 1
                l += 1

        return res if res else ""
