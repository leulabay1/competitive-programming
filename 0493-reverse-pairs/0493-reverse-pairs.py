class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        res = 0
        def mergeSort(left, right, arr):
            if left == right:
                return [arr[left]]
            mid = left + (right - left) // 2
            left_half = mergeSort(left, mid, arr)
            right_half = mergeSort(mid + 1, right, arr)
            pair_counter(left_half, right_half)
            return merge(left_half, right_half)
        def merge(left, right):

            p1 = p2 = 0
            arr = []
            while p1 < len(left) and p2 < len(right):
                if left[p1] <= right[p2]:
                    arr.append(left[p1])
                    p1 += 1
                else:
                    arr.append(right[p2])
                    p2 += 1
            arr += left[p1:]
            arr += right[p2:]
            return arr
        def pair_counter(left, right):
            nonlocal res
            i = len(left) - 1
            j = len(right) - 1
            while i >= 0 and j >= 0:
                if left[i] > 2 * right[j]:
                    res += j + 1
                    i -= 1
                else:
                    j -= 1
        
        mergeSort(0,len(nums)-1, nums)
        
        return res