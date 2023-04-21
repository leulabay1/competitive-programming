class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if s == '':
            return ''
        x = 0
        y = 0
        linestr_list = ['' for _ in range(numRows)]
        trav = 0
        while trav < len(s):
            while y < numRows:
                linestr_list[y] += s[trav]
                y = y + 1
                trav = trav + 1
                if trav == len(s):
                    return reduce(lambda x, y: x+y, linestr_list)
            y = y - 2
            while y > 0:
                linestr_list[y] += s[trav]
                y = y - 1
                trav = trav + 1
                if trav == len(s):
                    return reduce(lambda x, y: x+y, linestr_list)