class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        i = 0
        j = k-1
        no_sub = 0
        Sum = sum(arr[i:j+1])
         
        while j < len(arr):
            if Sum/k >= threshold:
                no_sub += 1
            j+=1
            if j < len(arr):
                Sum += arr[j]-arr[i]
            i+=1
        return no_sub