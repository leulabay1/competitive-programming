class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        oneRound = sum(chalk)
        if k >= oneRound:
            reminder = k%oneRound
        else:
            reminder = k
        index = 0 
        lastRound = 0
        for i in chalk:
            lastRound+=i
            if lastRound > reminder:
                return index
            index += 1