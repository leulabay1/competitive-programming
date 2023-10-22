class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        
        prefix = [0 for _ in range(len(arr) + 1)]
        prefix[0] = arr[0]
        cur = arr[0]
        for idx in range(len(arr)):
            prefix[idx + 1] = cur = cur ^ arr[idx]

        count = 0
            
        for i in range(len(arr) + 1):
            for j in range(i + 1, len(arr) + 1):
                for k in range(j + 1, len(arr) + 1):
                    if prefix[j] ^ prefix[i] == prefix[k] ^ prefix[j]:
                        count += 1
        return count