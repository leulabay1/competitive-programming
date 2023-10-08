class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        def dfs( curr ):
            
            if( curr in cache ):
                return cache[curr]
            
            my_set = set()
            for nei in graph[curr]:
                my_set = my_set.union( dfs( nei) )
            
            cache[curr] = my_set
            my_set.add(curr)
            return my_set
        
        graph = collections.defaultdict(list)
        for u,v in prerequisites:
            graph[u].append(v)
        
        cache = collections.defaultdict(set)
        for i in range(n):
            if i not in cache:
                dfs( i )
        
        ans = []
        for u,v in queries:
            ans.append( v in cache[u] )
        return ans 