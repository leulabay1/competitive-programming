class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr)< 3:
            return False
        i = 1
        while i < len(arr) and arr[i - 1] < arr[i]:
            i += 1
        if i == len(arr) or i == 1:
            return False
        while i < len(arr) and arr[i-1] > arr[i]:
            i += 1
        if i == len(arr):
            return True
        else:
            return False