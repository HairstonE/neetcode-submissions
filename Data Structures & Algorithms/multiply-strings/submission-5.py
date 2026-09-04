class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0": return "0"
        number1 = 0
        for num in num1:
            number1 = number1*10 + int(num)
        number2 = 0
        for num in num2:
            number2 = number2*10 + int(num)

        res_int = number1*number2
    
        res_str = ""
        while res_int:
            digit = res_int % 10
            res_int = res_int // 10
            res_str += str(digit)

        return "".join([c for c in reversed(res_str)])
