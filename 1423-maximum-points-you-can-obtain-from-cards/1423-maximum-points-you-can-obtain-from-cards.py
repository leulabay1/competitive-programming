class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        i = 0
        j = len(cardPoints)-k
        temp_sum = sum(cardPoints[j:])
        max_sum = temp_sum
        while j < len(cardPoints):
            temp_sum += cardPoints[i]-cardPoints[j]
            max_sum = max(max_sum, temp_sum)
            i+= 1
            j+= 1
        return max_sum