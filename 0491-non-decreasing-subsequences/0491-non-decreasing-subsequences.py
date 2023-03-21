class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backT(temp, i):
            if len(temp) >= 2:
                ans.append(temp.copy())
                
            visited = set()
            for j in range(i, len(nums)):
                if len(temp) > 0:
                    if nums[j] >= temp[-1] and nums[j] not in visited:
                        visited.add(nums[j])
                        temp.append(nums[j])
                        backT(temp, j + 1)
                        temp.pop()
                elif nums[j] not in visited:
                    visited.add(nums[j])
                    temp.append(nums[j])
                    backT(temp, j+1)
                    temp.pop()
        backT([], 0)
        return ans