class Solution:
    def findGCD(self, nums: List[int]) -> int:
        a = min(nums)
        b = max(nums)
        def gcd(b, a):
            if a == 0:
                return b
            return gcd(a, b%a)
        return gcd(b,a)