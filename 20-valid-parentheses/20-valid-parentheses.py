class Solution:
    def isValid(self, s: str) -> bool:
        temp = []
        for i in s:
            if i == '[' or i == '{' or i =='(':
                temp.append(i)
            else:
                if len(temp) == 0:
                    return False
                elif i ==')' and temp[len(temp)-1] == '(' :
                    temp.pop()
                elif i =='}' and temp[len(temp)-1] == '{' :
                    temp.pop()
                elif i ==']' and temp[len(temp)-1] == '[' :
                    temp.pop()
                else:
                    return False
        if len(temp) == 0:
            return True
        else:
            return False