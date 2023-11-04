class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        freq = Counter(nums)
        
        ans = -1
        freq_ = 0
        for ele in set(nums):
            if ele % 2 == 0 and freq_ < freq[ele]:
                ans = ele
                freq_ = freq[ele]
            if ele % 2 == 0 and freq_ == freq[ele]:
                ans = min(ans, ele)
                
        return ans