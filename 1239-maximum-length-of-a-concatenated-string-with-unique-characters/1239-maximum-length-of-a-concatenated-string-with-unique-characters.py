class Solution:
    def maxLength(self, arr: List[str]) -> int:
        g_max = 0
        
        def backT(freq, i):
            nonlocal g_max
            
            flag = False
            
            for j in range(i, len(arr)):
                flag = False
                temp = collections.Counter(arr[j])
                for char in temp:
                    if temp[char] > 1:
                        flag = True
                        break
                for char in temp:
                    if char in freq:
                        flag = True
                        break
                if flag:
                    continue
                    
                for char in temp:
                    freq[char] = 1
                    
                g_max = max(g_max, len(freq))
                backT(freq, j + 1)
                
                for char in temp:
                    del freq[char]
        backT({}, 0)
        return g_max
                
                
                