class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        res = set()
        def factors(num):
            i = 2
            while num > 1:
                if not num % i:
                    res.add(i)
                    num //= i
                else:
                    i += 1
            return res
        for num in nums:
            factors(num)
        return len(res)