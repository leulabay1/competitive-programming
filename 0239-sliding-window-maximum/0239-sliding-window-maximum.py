class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        que = []
        i = j = 0
        while j < len(nums):
            while que and que[-1] < nums[j]:
                que.pop()
            que.append(nums[j])
            if j >= k and nums[i-1] == que[0]:
                del que[0]
            if len(que) > k:
                del que[0]
            if j - i + 1 == k:
                ans.append(que[0])
            j += 1
            if j >= k:
                i += 1
        return ans
            