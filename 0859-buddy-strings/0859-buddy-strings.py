class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        n = len(s)
        m = len(goal)
        if n != m or n < 2:
            return False
        if s == goal:
            return len(s) - len(set(s)) >= 1
        dif = list()
        for i in range(n):
            if goal[i] != s[i]:
                dif.append(i)
                if len(dif) > 2:
                    return False
                
        if len(dif) == 2 and goal[dif[0]] == s[dif[1]] and goal[dif[1]] == s[dif[0]]:
            return True
        else:
            return False