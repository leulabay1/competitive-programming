class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        n = len(s)
        if n != len(goal) or n < 2:
            return False
        dif = list()
        for i in range(n):
            if goal[i] != s[i]:
                dif.append(i)
                
        if len(dif) == 2 and goal[dif[0]] == s[dif[1]] and goal[dif[1]] == s[dif[0]]:
            return True
        elif len(dif) == 0:
            freq = dict(Counter(s))
            for val in freq.values():
                if val > 1:
                    return True
            else:
                return False
        else:
            return False