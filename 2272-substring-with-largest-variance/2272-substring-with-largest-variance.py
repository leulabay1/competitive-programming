class Solution:
    def largestVariance(self, s: str) -> int:
        n = len(s)
        if not s:
            return 0
        ans = 0
        for i in range(ord('a'), ord('z') + 1, 1):
            a = chr(i)
            for j in range(ord('a'), ord('z') + 1, 1):
                b = chr(j)
                # a- b
                if a == b: continue
                diff = 0
                diff_with_b = float('-inf')
                for k, c in enumerate(s):
                    if c == a:
                        diff += 1
                        diff_with_b += 1
                    elif c == b:
                        diff -= 1
                        diff_with_b = diff
                        if diff < 0:
                            diff = 0
                    if diff_with_b > 0:
                        ans = max(ans, diff_with_b)
        return ans