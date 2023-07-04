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
                if not 1<<i & check:
                    check |= 1<<i
                    arr.append(nums[i])
                    backT(arr, check)
                    check &= ~(1<<i)
                    arr.pop()
            return
        backT([], 0)
        return ans