class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        groups = list()
        
        def check(str_1, str_2):
            count = 0
            for i in range(len(str_2)):
                if str_1[i] != str_2[i]:
                    count += 1
                if count > 2:
                    return False
            return True
        
        rank = {str_:1 for str_ in strs}
        UF = {}
        
        def find(str_):
            root = str_
            while UF[root] != root:
                root = UF[root]
            
            UF[str_] = root
            
            return root
        
        def union(str_1, str_2):
            
            pr1, pr2 = find(str_1), find(str_2)
            
            if pr1 != pr2:
                if rank[pr1] > rank[pr2]:
                    UF[pr2] = pr1
                    rank[pr1] += rank[pr2]
                else:
                    UF[pr1] = pr2
                    rank[pr2] += rank[pr1]
                
        
        for i in range(len(strs)):
            UF[strs[i]] = strs[i]
            
            for j in range(i):
                if check(strs[j], strs[i]):
                    union(strs[i], strs[j])
        
        return len(set([find(str_) for str_ in strs ]))
    