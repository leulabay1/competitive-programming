class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        cur_num = nums[-1]
        operation = 0
        
        if len(nums) <= 1:
            return 0
        
        for i in range(len(nums) - 2, -1, -1):
            if cur_num >= nums[i]:
                cur_num = nums[i]
            else:
                rem = nums[i]%cur_num
                operation += (math.ceil(nums[i]/cur_num) - 1)
                x = math.ceil(nums[i]/cur_num)
                cur_num = nums[i] // x
                
        return operation