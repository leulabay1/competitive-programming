class Solution:
    def numTeams(self, rating: List[int]) -> int:
        
        dp_for = [[1, 0, 0] for _ in range(len(rating))]
        dp_back = [[1, 0, 0] for _ in range(len(rating))]
        
        for i in range(len(rating)):
            for j in range(i):
                if rating[i] > rating[j]:
                    dp_for[i][1] += dp_for[j][0]
                    dp_for[i][2] +=  dp_for[j][1]
        for i in range(len(rating) - 1, -1, -1):
            for j in range(len(rating) - 1, i, -1):
                if rating[i] > rating[j]:
                    dp_back[i][1] += dp_back[j][0]
                    dp_back[i][2] +=  dp_back[j][1]
        ans = 0
        print(dp_for, dp_back)
        
        for tri1, tri2 in zip(dp_for, dp_back):
            ans += (tri1[2] + tri2[2])
        
        return ans