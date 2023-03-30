class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]*(n+1)
        for nums in range(n+1):
            org = nums
            val = nums&1
            nums >>= 1
            ans[org] = ans[nums] + val
        return ans