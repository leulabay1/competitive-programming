class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        dp = []
        
        if n < 3:
            return 0
        
        ans = 0
        i = 1
        while i < n:
            size = 1
            dif = nums[i] - nums[i - 1]
            while i < n and nums[i] - nums[i - 1] == dif:
                size += 1
                i += 1
            if size >= 3:
                ans += ((size - 1)*(size - 2)/2)
        return int(ans)