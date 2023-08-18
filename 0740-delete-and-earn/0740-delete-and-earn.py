class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        freq = Counter(nums)
        n = len(freq)
        nums.sort()
        nums = list(set(nums))
        dp = {}
        ans = 0
        def backT(i, val):
            nonlocal n
            maxChild = 0
            if i == n-1:
                dp[nums[i]] = nums[i]*freq[nums[i]]
            
            if nums[i] in dp:
                return dp[nums[i]]
            
            for j in range(i + 1, n):
                if nums[j] != nums[i] + 1:
                    if nums[j] in dp:
                        maxChild = max(dp[nums[j]], maxChild)
                    else:
                        val += (nums[j] * freq[nums[j]])
                        maxChild = max(backT(j, val), maxChild)
                        val -= (nums[j] * freq[nums[j]])
            dp[nums[i]] = maxChild + (nums[i] * freq[nums[i]])
            return dp[nums[i]]
        for i in range(n):
            ans = max(backT(i, 0), ans)
        return ans