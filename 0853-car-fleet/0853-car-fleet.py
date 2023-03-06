class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = []
        for i in range(len(speed)):
            time.append([position[i], (target-position[i])/speed[i]])
        
        time.sort(reverse=True)
        
        ans = 0
        stack = [time[0]]
        for i in range(1, len(time)):
            if stack and time[i][1] > stack[-1][1]:
                while stack and time[i][1] > stack[-1][1]:
                    stack.pop()
                if len(stack) == 0:
                    ans += 1
            stack.append(time[i])
        
        return ans if len(stack) == 0 else ans+1