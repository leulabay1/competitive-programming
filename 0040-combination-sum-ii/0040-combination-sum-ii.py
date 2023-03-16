class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def combine(nums, s, idx):
            if s == target:
                nums_ = nums.copy()
                ans.append(nums_)
                return
            if idx >= len(candidates) or s > target or (target-s) < candidates[idx]:
                return
            visited = set()
            for i in range(idx,len(candidates)):
                if candidates[i] not in visited:
                    visited.add(candidates[i])
                    nums.append(candidates[i])
                    s += candidates[i]
                    combine(nums, s, i+1)
                    nums.pop()
                    s -= candidates[i]
                
        candidates.sort()
        combine([], 0, 0)
        return ans