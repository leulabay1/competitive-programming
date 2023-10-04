class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        i = 0
        sum_ = 0
        ans = 0
        
        for j in range(len(nums)):
            sum_ += nums[j]
            while i <= j and (j - i + 1) * sum_ >= k:
                sum_ -= nums[i]
                i += 1
            
            cur_leng = j - i + 1
            prev_val = (cur_leng * (cur_leng - 1))//2
            cur_val = ((cur_leng + 1) * cur_leng)//2
            ans += cur_val - prev_val
        
        return ans
            