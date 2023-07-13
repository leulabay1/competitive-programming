class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        primes = []

        is_prime = [False,False] + [True]*(right-1)

        for p in range(2,right+1):
            if is_prime[p]:
                primes.append(p)

                for i in range(2*p,right+1,p):
                    is_prime[i] = False

        ans = [i for i in primes if left <= i <= right]

        if len(ans) < 2:
            return [-1,-1]

        dict1 = collections.defaultdict(int)

        for i in range(1,len(ans)):
            dict1[(ans[i-1],ans[i])] = ans[i] - ans[i-1]

        min_val = min(dict1.values())

        return [i for i in dict1 if dict1[i] == min_val][0]