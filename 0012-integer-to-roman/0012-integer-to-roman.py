class Solution:
    def intToRoman(self, num: int) -> str:
        val1 = [1000, 500, 100, 50, 10, 5]
        val2 = [900, 400, 90, 40, 9, 4]
        sym1 = ["M", "D", "C", "L", "X", "V"]
        sym2 = ["CM", "CD", "XC", "XL", "IX", "IV"]
        res = ""
        for i in range(6):
            q,  r = divmod(num, val1[i])
            if q > 0:
                res += q*sym1[i]
                num = r
            if num >= val2[i]:
                res += sym2[i]
                num -= val2[i]
            if num == 0:
                return res
        if num > 0:
            res += num*"I"
        return res