class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i = 0
        n = len(nums)
        while i < len(nums):
            if nums[i] != i + 1:
                num1 = nums[i]
                if nums[num1-1] == num1:
                    i+=1
                    continue
                nums[i] = nums[num1-1]
                nums[num1-1] = num1
                continue
            i+=1
        
        ans = []
        for i in range(n):
            if i+1 != nums[i]:
                ans.append(i+1)
        return ans