class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        pushp = 0
        popp = 0
        while pushp < len(pushed):
            stack.append(pushed[pushp])
            while stack and stack[len(stack)-1] == popped[popp]:
                stack.pop()
                popp+=1
            pushp+=1
        return False if stack else True