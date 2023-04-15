class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c == 0:
            return True
        for i in range(c):
            a = i * i
            b = c - a
            if b < a:
                return False
            else:
                sq = math.sqrt(b)
                if sq == int(sq):
                    return True