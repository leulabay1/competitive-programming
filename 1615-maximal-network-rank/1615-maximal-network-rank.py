class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        nodes = defaultdict(set)
        for edge in roads:
            nodes[edge[0]].add(edge[1])
            nodes[edge[1]].add(edge[0])
        
        ans = 0
        i = 0
        nodes = dict(nodes)
        nodes = list(nodes.items())
        print(nodes)
        for i in range(len(nodes)-1):
            for j in range(i+1, len(nodes)):
                if nodes[i][0] in nodes[j][1]:
                    ans = max(ans, len(nodes[i][1]) + len(nodes[j][1]) - 1)
                else:
                    ans = max(ans, len(nodes[i][1]) + len(nodes[j][1]))
        return ans