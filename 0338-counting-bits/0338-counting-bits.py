class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        ans = [0]
        cou = 1
        leng = 1
        while cou <= n: 
            for i in range(leng):
                if cou > n:
                    break
                ans.append(1 + ans[i])
                cou += 1
            leng *= 2
        return ans