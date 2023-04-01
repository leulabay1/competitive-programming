class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = 0
        p2 = 0
        temp = nums1[:m]
        res = []
        while p1 < m and p2 < n:
            if temp[p1] > nums2[p2]:
                res.append(nums2[p2])
                p2 += 1
            else:
                res.append(temp[p1])
                p1 += 1
        res += temp[p1:]
        res += nums2[p2:]
        nums1[:] = res