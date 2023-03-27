class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
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
            n = len(right)
            nonlocal res
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i] - right[j] <= diff:
                    res += n - j
                    i += 1
                else:
                    j += 1
        
        nums3 = []
        for i in range(len(nums1)):
            nums3.append(nums1[i]-nums2[i])
        mergeSort(0,len(nums3)-1, nums3)
        
        return res
                
                
                
                
            
            