class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def palindrom_checker(sub):
            for i in range(len(sub)//2):
                if sub[i] != sub[len(sub) - i - 1]:
                    return False
            return True
            
        ans = []
        
        def dp(i, arr):
            if i >= len(s):
                ans.append(arr.copy())
                return
            for idx in range(i + 1, len(s) + 1):
                if palindrom_checker(s[i:idx]):
                    arr.append(s[i:idx])
                    dp(idx, arr)
                    arr.pop()
        
        dp(0, [])
        return ans