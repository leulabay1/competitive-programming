class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        sorted_players = sorted(zip(ages, scores))
        answer = 0
        picked_players = []

        for player in sorted_players:
            max_score = 0
            for picked_player in picked_players:
                  if picked_player[1] <= player[1]:
                        max_score = max(max_score, picked_player[0])
            picked_players.append((max_score + player[1], player[1]))
            answer = max(answer, max_score + player[1])

        return answer