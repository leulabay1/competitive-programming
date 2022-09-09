class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        arr.sort()
        dict1 = {}
        temp = -1
        ctr = 0
        for i in arr:
            if temp != i:
                dict1[temp] = ctr
                temp = i
                ctr = 1
            else:
                ctr += 1
        dict1[temp] = ctr
        del dict1[-1]
        sorted_dict = {key: val for key, val in sorted(dict1.items(), key = lambda ele: ele[1], reverse = True)}
        
        size = 0
        ctr = 1
        for i in sorted_dict.values():
            if size+i >= len(arr)//2:
                return ctr
            else:
                ctr += 1
                size += i