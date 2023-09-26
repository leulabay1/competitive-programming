class Solution:
    def maxAbsoluteSum(self, A: List[int]) -> int:
        return max(accumulate(A, initial=0)) - min(accumulate(A, initial=0))