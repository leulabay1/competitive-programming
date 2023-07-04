class Solution:
    def findComplement(self, num: int) -> int:
        result = 0
        mask = 1
        n = len(bin(num))-2
        for i in range(n):
            temp = (mask << i) & num
            result = result | 1 << i if not temp else result
        return result
            