class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        def wordBreakHelp(i: int) -> bool:
            if i == len(s):
                return True
            res = False
            for word in wordDict:
                if (word, i) in memo: return memo[(word, i)]
                if word == s[i : i + len(word)]:
                   
                    res |= wordBreakHelp(i + len(word))
                    memo[(word, i)] = res

            return res

        return wordBreakHelp(0)
