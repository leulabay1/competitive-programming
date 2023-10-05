class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        ans = set()
        def backT(i, arr):
            if tuple(arr) not in ans:
                ans.add(tuple(arr))
            
            for j in range(i, len(nums)):
                arr.append(nums[j])
                backT(j + 1, arr)
                arr.pop()
        backT(0, [])
        
        return list(ans)