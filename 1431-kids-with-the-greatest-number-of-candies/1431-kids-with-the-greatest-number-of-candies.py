class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        maxCand = max(candies)
        for cand in candies:
            if cand + extraCandies >= maxCand:
                result.append(True)
            else:
                result.append(False)
        return result