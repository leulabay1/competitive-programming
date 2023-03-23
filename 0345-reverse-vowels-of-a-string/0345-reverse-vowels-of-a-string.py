class Solution:
    def reverseVowels(self, s: str) -> str:
        vouls = set(["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"])
        index = []
        s_list = []
        con = 0
        for i in s:
            if i in vouls:
                index.append(con)
            s_list.append(i)
            con += 1
        
        for i in range(len(index)//2):
            temp = s_list[index[i]]
            s_list[index[i]] = s_list[index[len(index)-i-1]]
            s_list[index[len(index)-i-1]] = temp
        return "".join(s_list)