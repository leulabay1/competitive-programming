class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        result = []
        if len(nums)%2 == 0:
            for i in range(len(nums)//2):
                result.append(nums[i+len(nums)//2])
                result.append(nums[i])
                
        else:
            for i in range(len(nums)//2):
                result.append(nums[i+len(nums)//2])
                result.append(nums[i])
            result.append(nums[len(nums)-1])
            
        return result