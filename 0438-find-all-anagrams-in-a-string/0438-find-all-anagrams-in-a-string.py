class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(s) < len(p): return []
        p_dict = {}
        s_dict = {}
        for i in range(len(p)):
            p_dict[p[i]] = 1+p_dict.get(p[i],0)
            s_dict[s[i]] = 1+s_dict.get(s[i],0)
        
        res =[]
        if p_dict == s_dict:
            res.append(0)
        
        lp = 0
        for rp in range(len(p), len(s)):
            s_dict[s[rp]] = 1 + s_dict.get(s[rp],0)
            s_dict[s[lp]] = s_dict.get(s[lp]) - 1
            
            if s_dict[s[lp]] == 0:
                s_dict.pop(s[lp])
            if s_dict == p_dict:
                res.append(lp+1)
            lp += 1
        return res