class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        return len(set(nums) | {int(str(n)[::-1]) for n in nums})