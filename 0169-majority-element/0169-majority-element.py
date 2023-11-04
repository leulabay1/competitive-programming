class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = Counter(nums)
        
        set_ = set(nums)
        
        for ele in set_:
            if freq[ele] > len(nums)//2:
                return ele