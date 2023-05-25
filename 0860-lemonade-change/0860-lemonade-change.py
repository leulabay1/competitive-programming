class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        changes = [0, 0]
        
        for i in bills:
            if i == 10:
                if changes[0]:
                    changes[1] += 10
                    changes[0] -= 5
                else:
                    return False
            elif i == 20:
                if changes[1] and changes[0]:
                    changes[1] -= 10
                    changes[0] -= 5
                elif changes[0] >= 15:
                    changes[0] -= 15
                else:
                    return False
            else:
                changes[0] += 5
        return True