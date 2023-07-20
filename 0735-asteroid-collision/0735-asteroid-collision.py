class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        flag = True
        for asteroid in asteroids:
            while stack and stack[-1] > 0 and asteroid < 0 :
                if abs(stack[-1]) < abs(asteroid):
                    stack.pop()
                elif abs(stack[-1]) == abs(asteroid):
                    stack.pop()
                    flag = False
                    break
                else:
                    flag = False
                    break
            if flag:
                stack.append(asteroid)
            else: flag = True
            
        return stack