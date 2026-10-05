class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        strs.sort(key=lambda w: len(w))

        res = ""
        
        word = strs[0]
        for i, c in enumerate(word): 
            if all([s[i] == c for s in strs]):
                res += c
            else:
                break

        return res