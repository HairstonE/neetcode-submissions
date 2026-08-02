class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        letters = set()
        res = 0
        while r < len(s):
            while s[r] in letters and l <= r:
                letters.remove(s[l])
                l += 1
        
            letters.add(s[r])
            res = max(res, len(letters))
                
            r += 1
        return res