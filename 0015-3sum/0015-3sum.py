class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        posDict = defaultdict(set)
        for i in range(len(nums)):
            posDict[nums[i]].add(i)
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if posDict[-1*(nums[i] + nums[j])]:
                    flag = False
                    if len(posDict[-1*(nums[i] + nums[j])]) > 2:
                        flag = True
                    else:
                        coun = 0
                        for num in posDict[-1*(nums[i] + nums[j])]:
                            if num == i or num == j:
                                coun += 1
                        if coun != len(posDict[-1*(nums[i] + nums[j])]):
                            flag = True
                    if flag:
                        tobeAppend = (-1*(nums[i] + nums[j]), nums[i], nums[j])
                        tobeAppend = tuple(sorted(tobeAppend))
                        if tobeAppend not in ans:
                            ans.add(tobeAppend)
                  
        return list(ans)