class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for i in s:
            if i != ")":
                stack.append(i)
            else:
                tempS = ""
                pop_val = stack.pop()
                while pop_val != "(":
                    tempS += pop_val
                    pop_val = stack.pop()
                    
                for j in tempS:
                    stack.append(j)
        res = ""
        for i in stack:
            res += i
        
        return res