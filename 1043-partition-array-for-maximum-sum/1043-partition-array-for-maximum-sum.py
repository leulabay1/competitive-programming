class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        N = len(arr) 
        @cache
        def dp(idx):              
            max_num = max_sum = 0
            for i in range(idx, min(idx + k, N)):
                max_num = max(max_num, arr[i])
                max_sum = max(max_sum, (i - idx + 1) * max_num + dp(i + 1))
                
            return max_sum
        
        return dp(0)