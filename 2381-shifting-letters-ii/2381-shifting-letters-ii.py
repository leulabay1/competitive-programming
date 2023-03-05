class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        pref = [0]*(len(s) + 1)
        for start, end, direction in shifts:
            direc = 1 if direction else -1
            
            pref[start] += direc
            pref[end+1] -= direc
        
        shifSum = 0
        for i in range(len(pref)):
            shifSum += pref[i]
            pref[i] = shifSum
        print(pref)
        
        ans = []
        for i in range(len(s)):
            ordOfi = ord("a") + (((ord(s[i]) + pref[i]) - ord("a")) % 26)
            ans.append(chr(ordOfi))
        
        return "".join(ans)
            