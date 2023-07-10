class Solution:
    def rob(self, arr: List[int]) -> int:
        
        def helper(nums):
            rob1, rob2 = 0, 0
            for num in nums:
                temp = max(num + rob1, rob2)
                rob1 = rob2
                rob2 = temp

            return rob2
        return max(arr[0], helper(arr[1:]), helper(arr[0:-1]))