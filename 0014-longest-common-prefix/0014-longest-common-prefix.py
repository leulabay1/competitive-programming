class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = strs[0]
        for i in strs[1:]:
            temp = ""
            l = 0
            n = min(len(i),len(ans))
            while l < n:
                if ans[l] == i[l]:
                    temp += ans[l]
                else:
                    break
                l += 1
            ans = temp
            if temp == "":
                break
        return ans