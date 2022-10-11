class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixPro = [1]
        pro = 1
        for i in nums:
            pro*=i
            prefixPro.append(pro)
        
        sufixPro = [1]
        pro = 1
        for i in range(len(nums)-1):
            pro*=nums[len(nums)-1-i]
            sufixPro.insert(0,pro)
        
        res = []
        for i in range(len(nums)):
            res.append(prefixPro[i]*sufixPro[i])
        
        return res