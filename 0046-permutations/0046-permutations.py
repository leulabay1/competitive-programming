class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        def backT(arr, check):
            nonlocal n
            if len(arr) == n:
                ans.append(arr.copy())
                return
            for i in range(n):
                if i not in check:
                    check.add(i)
                    arr.append(nums[i])
                    backT(arr, check)
                    check.remove(i)
                    arr.pop()
            return
        backT([], set())
        return ans