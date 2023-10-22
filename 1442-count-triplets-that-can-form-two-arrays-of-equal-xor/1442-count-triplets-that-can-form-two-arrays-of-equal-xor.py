class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        
        prefix_xor = [None for _ in range(len(arr) + 1)]
        prefix_xor[0] = arr[0]
        
        for idx in range(len(arr)):
            prefix_xor[idx + 1] = prefix_xor[idx] ^ arr[idx]

        count = 0
            
        for i in range(len(arr) + 1):
            for j in range(i + 1, len(arr) + 1):
                for k in range(j + 1, len(arr) + 1):
                    if prefix_xor[j] ^ prefix_xor[i] == prefix_xor[k] ^ prefix_xor[j]:
                        count += 1
        return count