class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        max_defense = 0
        ans = 0
        properties.sort(key = lambda x: (-x[0], x[1]))

        for attack, defense in properties:
            if defense < max_defense:
                ans += 1
            max_defense = max(max_defense, defense)

        return ans