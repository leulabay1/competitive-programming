class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans = []
        k = floor(len(nums)/3)
        
        freqDict = Counter(nums)
        
        for num, freq in freqDict.items():
            if freq > k:
                ans.append(num)
        return ans