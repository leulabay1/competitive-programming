class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def combine(nums, s, idx):
            if s == target:
                nums_ = nums.copy()
                ans.append(nums_)
                return
            if s > target:
                return
            
            for i in range(idx,len(candidates)):
                nums.append(candidates[i])
                s += candidates[i]
                combine(nums, s, i)
                nums.pop()
                s -= candidates[i]
        combine([], 0, 0)
        return ans