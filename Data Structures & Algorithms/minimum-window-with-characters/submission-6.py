class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = Counter(t) 
        s_count = defaultdict(int) 
        res = None
        l = 0
        for r in range(len(s)):
            s_count[s[r]] += 1 
            while all([t_count[c] <= s_count[c] for c in t_count]):
                if res == None or (r - l + 1) < len(res):
                    res = s[l:r+1]
                s_count[s[l]] -= 1
                l += 1

        for i in range(l, len(s)):
            s_count[s[i]] -= 1
            if all([t_count[c] <= s_count[c] for c in t_count]):
                if res == None or (r - i + 1) < len(res):
                    res = s[i + 1:r+1]
                
            
        return res if res else ""