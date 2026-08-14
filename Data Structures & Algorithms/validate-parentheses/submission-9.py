class Solution:
    def isValid(self, s: str) -> bool:
        parens = {
          "]" : "[",
           "}" : "{",
           ")" : "("
        }
        stack = []
        for c in s:
            if c in parens.values():
                stack.append(c)
            else:
                if stack and stack[-1] == parens[c]:
                    stack.pop()
                else:
                    return False
        return not stack
            
