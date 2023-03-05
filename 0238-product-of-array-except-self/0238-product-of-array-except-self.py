class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixPro = [1]
        pro = 1
        for i in nums:
            pro*=i
            prefixPro.append(pro)
        
        sufixPro = [1]
        pro = 1
        for i in range(len(nums)):
            pro*=nums[len(nums)-i-1]
            sufixPro.insert(0,pro)
            
        answer = []
        for i in range(len(nums)):
            answer.append(prefixPro[i]*sufixPro[i+1])
        
        return answer