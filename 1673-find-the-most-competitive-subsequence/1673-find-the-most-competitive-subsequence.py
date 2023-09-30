class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        remove_num_elements = len(nums) - k
    
        stack = []

        for index, num in enumerate(nums):
            while stack and remove_num_elements and nums[stack[-1]] > nums[index]:
                stack.pop()
                remove_num_elements -= 1

            stack.append(index)

        return [nums[i] for i in stack][:k]