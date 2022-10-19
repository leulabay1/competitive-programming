class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ans = 0
        stack = []
        times = [float(target - p) / s for p, s in sorted(zip(position, speed), reverse=True)]
        
        for time in times:
            stack.append(time)
            if len(stack) >= 2 and stack[-2] >= stack[-1]:
                stack.pop()

        return len(stack)