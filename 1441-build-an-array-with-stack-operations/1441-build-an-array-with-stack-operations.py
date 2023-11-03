class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        max_val = max(target)
        target = set(target)
        
        ans = []
        for i in range(1, max_val + 1):
            if i not in target:
                ans.append("Push")
                ans.append("Pop")
            else:
                ans.append("Push")
                
        return ans
                