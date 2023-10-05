class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        def backT(i, visited, arr):
            if len(arr) == len(nums) and tuple(arr) not in ans:
                ans.add(tuple(arr))
            
            for j in range(len(nums)):
                if j not in visited:
                    visited.add(j)
                    arr.append(nums[j])
                    backT(j, visited, arr)
                    visited.remove(j)
                    arr.pop()
        backT(0, set(), [])
        
        return list(ans)