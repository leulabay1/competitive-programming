class Solution:
    def countAndSay(self, n: int) -> str:
        def sequence(cun, ans):
            if cun == n:
                return ans
            i = 0
            temp = ""
            while i < len(ans):
                val = ans[i]
                j = i
                while j < len(ans) and ans[j] == val:
                    j += 1
                temp += str(j - i)
                temp += ans[i]
                i = j
            return sequence(cun + 1, temp)
        return sequence(1, "1")