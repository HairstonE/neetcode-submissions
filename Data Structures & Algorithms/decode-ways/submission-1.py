class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}

        def decodeHelper(i: int):
            if i >= len(s): 
                return 1

            if i in memo:
                return memo[i]

            res = 0
            if int(s[i]) > 0:
                res += decodeHelper(i + 1)
            if i + 1 < len(s) and 10 <= int(s[i] + s[i+1]) <= 26:
                res += decodeHelper(i + 2)
            memo[i] = res
            return res



        return decodeHelper(0)
            


        