class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            # print("-11".isdigit())
            if t.lstrip('-').isdigit():
                stack.append(int(t))
            else:
                a = stack.pop()
                b = stack.pop()

                if t == "+":
                    stack.append(a+b)
                elif t == "-":
                    stack.append(b-a)
                elif t == "*":
                    stack.append(a*b)
                else:
                    stack.append(int(b/a))
        return stack[-1]

