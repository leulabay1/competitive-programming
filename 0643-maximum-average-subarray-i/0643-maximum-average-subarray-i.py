class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        right = k-1
        test = float("inf")
        ans = sum(nums[left:right+1])/k
        temp = sum(nums[left:right+1])
        while right+1 < len(nums):
            temp += nums[right+1]
            temp -= nums[left]
            ans = max(ans, temp/k)
            right += 1
            left += 1

        return ans