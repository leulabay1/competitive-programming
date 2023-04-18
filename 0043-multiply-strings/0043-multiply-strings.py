class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        ans = 0
        num2 = int(num2)
        mult = 1
        for digit in num1[::-1]:
            ans += num2 *int(digit)*mult
            mult *= 10
        return str(ans)