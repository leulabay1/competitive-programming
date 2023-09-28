class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        ans = []
        primes = [1] * ((n >> 1) + 1)
        print(10 >> 1)
        is_prime = lambda x: x == 2 or (x & 1 and primes[x >> 1])

        p = 3
        while p * p <= n:
            if not primes[p >> 1]:
                p += 2
                continue
            
            
            for i in range(p * p, n + 1, p * 2):
                primes[i >> 1] = 0
  
            p += 2

        if n >= 4 and is_prime(n - 2): ans.append([2, n - 2])
        
        for num in range(3, n // 2 + 1, 2):
            target = n - num

            if is_prime(num) and is_prime(target):
                ans.append([num, target])

        return ans