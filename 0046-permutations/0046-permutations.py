class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        def Tracker(arr, visited, i):
            nonlocal n
            if len(arr) == n:
                ans.append(arr.copy())
                return
            for j in range(n):
                if j not in visited:
                    visited.add(j)
                    arr.append(nums[j])
                    Tracker(arr, visited, j)
                    arr.pop()
                    visited.remove(j)
        Tracker([], set(), -1)
        return ans