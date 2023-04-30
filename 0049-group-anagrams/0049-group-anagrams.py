class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        graph =  collections.defaultdict(list)

        for i in strs:
            key = tuple(sorted(collections.Counter(i).items()))
            graph[key].append(i)

        return graph.values()