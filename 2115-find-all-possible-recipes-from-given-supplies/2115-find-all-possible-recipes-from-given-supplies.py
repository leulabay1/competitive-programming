class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supplies = set(supplies)
        graph = {i:set() for i in recipes}
        for i in range(len(recipes)):
            for ing in ingredients[i]:
                if ing not in supplies:
                    graph[recipes[i]].add(ing)
        ans = set()
        for node in graph:
                if len(graph[node]) == 0:
                    ans.add(node)
        print(graph)  
        for i in range(len(recipes)):
            for node in graph:
                temp = graph[node].copy()
                for nei in temp:
                    if nei in ans:
                        graph[node].remove(nei)
                if len(graph[node]) == 0 not in ans:
                    ans.add(node)
        return list(ans)
                    
            