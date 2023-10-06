class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        stack = []
        cur = []
        
        for i in range(len(s)):
                    
            if cur and cur[-1] == s[i]:
                cur.append(s[i])
            else:
                cur = [s[i]]
                
            stack.append(s[i])
            
            if len(cur) == k:
                for _ in range(k):
                    letter = stack.pop()
                    
                j = len(stack) - 1
                cur = [stack[-1]] if stack else []
                while stack and j > 0 and stack[j] == stack[j - 1]:
                    cur.append(stack[-1])
                    j -= 1
            
        return "".join(stack)