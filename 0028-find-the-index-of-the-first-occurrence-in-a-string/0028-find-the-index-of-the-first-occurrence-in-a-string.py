class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = j = 0
        if len(haystack)<len(needle):
            return -1
        while j < len(haystack):
            if haystack[j] == needle[0]:
                ctr = 0
                while j < len(haystack) and ctr < len(needle) and haystack[j] == needle[ctr]:
                    if ctr == len(needle)-1:
                        return i
                    j+=1
                    ctr+=1
            i+=1
            j=i
        return -1
    