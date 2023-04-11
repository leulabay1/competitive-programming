class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        ans = []
        def DFS(node, end, arr):
            if node == end:
                ans.append(arr.copy())
                return
            for adj in graph[node]:
                arr.append(adj)
                DFS(adj, end, arr)
                arr.pop()
        DFS(0, n-1, [0])
        return ans