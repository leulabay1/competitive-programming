class Solution:
    def minSwaps(self, s: str) -> int:
        count = 0
        for ch in s:
            if ch=='[':
                count += 1
            elif ch==']' and count>0:
                count -= 1
                
        return ceil(count/2)