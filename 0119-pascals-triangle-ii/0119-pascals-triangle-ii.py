class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]
        else:
            row = self.getRow(rowIndex-1)
            ans = [0]*(rowIndex+1)
            ans[0] = 1
            ans[-1] = 1
            for i in range(1, len(row)):
                ans[i] = row[i-1] + row[i]
            return ans
                
                