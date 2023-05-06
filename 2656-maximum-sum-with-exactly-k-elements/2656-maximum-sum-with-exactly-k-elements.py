class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        nums.sort()
        return (nums[-1] * k) + (k-1)*k//2