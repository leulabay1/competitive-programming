class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        def reverse(s, i):
            if i >= len(s)//2:
                return s
            else:
                temp = s[len(s)-1-i]
                s[len(s)-1-i] = s[i]
                s[i] = temp
                reverse(s,i+1)
        reverse(s,i)