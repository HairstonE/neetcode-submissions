class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        new_num = 0
        num = x

        while x: 
            digit = x % 10 
            x = x // 10
            new_num = 10 * new_num + digit

        print(new_num)

        return new_num == num