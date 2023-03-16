class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        map_ = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        ans = []
        def combine(arr, n):
            if n >= len(digits):
                ans.append("".join(arr))
                return
            for i in map_[digits[n]]:
                arr.append(i)
                combine(arr, n+1)
                arr.pop()
                
        if len(digits) == 0:
            return ans
        
        combine([], 0)
        return ans
                