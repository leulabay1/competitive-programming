class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        freq = dict(Counter(nums))

        if k == 0:
            ans = 0
            for key in freq.keys():
                if freq[key] > 1:
                    ans += 1
            return ans

        nums = list(sorted(list(set(nums))))
        ans = 0
        i = 0
        j = 1
        while i < len(nums) and j < len(nums):
            if i == j:
                j += 1
                continue
            if abs(nums[i] - nums[j]) == k:
                ans += 1
                i += 1
                j += 1
            elif abs(nums[i] - nums[j]) < k:
                j += 1
            else:
                i += 1
        return ans