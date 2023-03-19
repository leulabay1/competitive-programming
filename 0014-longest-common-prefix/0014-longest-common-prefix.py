class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = strs[0]
        for i in strs[1:]:
            temp = ""
            n = min(len(i),len(ans))
            for l in range(n):
                if ans[l] == i[l]:
                    temp += ans[l]
                else:
                    break
            ans = temp
            if temp == "":
                break
        return ans