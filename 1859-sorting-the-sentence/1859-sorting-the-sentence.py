class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        a = s.split(" ")
        b = []
        for j in range(len(a)):
            for i in a:
                if int(i[-1]) == j+1:
                    b.append(i[:len(i)-1])
                    break
        result = ""
        for i in b:
            result += i
            result += " "
        return result[:-1]
            