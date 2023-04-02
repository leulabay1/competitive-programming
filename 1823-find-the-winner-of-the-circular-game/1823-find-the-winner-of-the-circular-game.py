class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = list(range(1, n+1))
        i = 0
        while len(friends) > 1:
            if i > len(friends) - 1:
                i %= len(friends) 
            delete = i + k - 1
            if delete > len(friends) - 1:
                delete %= (len(friends))
            del friends[delete]
            i = delete
        return friends[0]