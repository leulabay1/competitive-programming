class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        set_char = set()
        j = 0
        res = 0
        for i in range(len(s)):
            while s[i] in set_char:
                set_char.remove(s[j])
                j+=1
            set_char.add(s[i])
            res = max(res, len(set_char))
        return res