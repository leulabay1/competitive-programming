class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        i = 0
        ans = set()
        while i < len(nums):
            if nums[i] != i + 1:
                num1 = nums[i]
                if nums[num1-1] == num1:
                    ans.add(num1)
                    i+=1
                    continue
                nums[i] = nums[num1-1]
                nums[num1-1] = num1
                continue
            i+=1
        ans = list(ans)
        for i in range(len(nums)):
            if i + 1 != nums[i]:
                ans.append(i+1)
        return ans