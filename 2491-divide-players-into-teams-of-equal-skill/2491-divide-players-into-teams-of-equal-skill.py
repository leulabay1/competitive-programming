class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        res = 0
        flag = skill[0]+skill[len(skill)-1]
        for i in range(len(skill)//2):
            if flag != skill[i]+skill[len(skill)-i-1]:
                return -1
            res += skill[i]*skill[len(skill)-i-1]
        return res