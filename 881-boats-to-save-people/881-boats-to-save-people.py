class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        a = 0
        b = 1
        a, b = 0, len(people) - 1
        ans = 0
        while a <= b:
            ans += 1
            if people[a] + people[b] <= limit:
                a += 1
            b -= 1
        return ans