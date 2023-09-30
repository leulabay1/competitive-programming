class Solution:
    def balancedString(self, s: str) -> int:
        cnt = Counter(s)
        avg = (len(s) // 4)
        
        for ch in list(cnt.keys()):
            cnt[ch] -= avg
            if cnt[ch] <= 0: del cnt[ch]
        
        # keep track of the number of corretions we have to make
        corrections = sum(cnt.values())
        if not corrections: return 0
        
        left = 0
        min_s = len(s) + 1
        for right, ch in enumerate(s):
            if ch in cnt:
                cnt[ch] -= 1
                corrections -= cnt[ch] >= 0
            while (s[left] not in cnt or cnt[s[left]] < 0) and left < right:
                if s[left] in cnt:
                    cnt[s[left]] += 1
                left += 1
            if corrections == 0:
                min_s = min(min_s, right - left + 1)
            
        return min_s