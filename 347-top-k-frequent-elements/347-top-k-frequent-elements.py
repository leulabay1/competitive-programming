class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        dict1 = {}
        temp = "a"
        ctr = 0
        for i in nums:
            if temp != i:
                dict1[temp] = ctr
                temp = i
                ctr = 1
            else:
                ctr += 1
        dict1[temp] = ctr
        del dict1["a"]
        sorted_dict = {key: val for key, val in sorted(dict1.items(), key = lambda ele: ele[1], reverse = True)}
        
        ctr1 = 1
        result = []
        for i in sorted_dict.keys():
            result.append(i)
            ctr1 += 1
            if ctr1 > k:
                break
        return result