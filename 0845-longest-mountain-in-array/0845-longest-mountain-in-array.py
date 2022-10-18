class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        if n < 3:
            return 0
        ans = 0
        i = j = 0
        while j < n-1:
            j+=1
            if arr[j]>arr[i]:
                while j < n and arr[j-1] < arr[j]:
                    j+=1
                temp = j
                while j < n and arr[j-1] > arr[j]:
                    j+=1
                if temp < j:
                    ans = max(ans, j-i)
                j = j-1
            i = j
        return ans
            