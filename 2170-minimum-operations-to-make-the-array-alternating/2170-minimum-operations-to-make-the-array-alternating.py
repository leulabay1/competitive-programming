class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        even_indecies = []
        odd_indecies = []
        
        for i in range(len(nums)):
            
            if i % 2 == 0:
                even_indecies.append(nums[i])
            else:
                odd_indecies.append(nums[i])
                
        freq_even = sorted(dict(Counter(even_indecies)).items(), key = lambda x: x[1])
        freq_odd = sorted(dict(Counter(odd_indecies)).items(), key = lambda x: x[1])
        
        print(freq_odd, freq_even)
        
        if freq_even[-1][0] != freq_odd[-1][0]:
            return (ceil(len(nums)/2) - freq_even[-1][-1]) + (len(nums)//2 - freq_odd[-1][-1])
        
        else:
            if len(nums) == 2 and nums[0] == nums[1]:
                return 1
            if len(nums) == 2 and nums[0] != nums[1]:
                return 0
            
            
            
            if (freq_even[-1][-1] > freq_odd[-1][-1] or freq_even[-1][-1] <= freq_odd[-1][-1])  and len(freq_even) > 1 and len(freq_odd) > 1 :
                return min((ceil(len(nums)/2) - freq_even[-2][-1]) + (len(nums)//2 - freq_odd[-1][-1]), (ceil(len(nums)/2) - freq_even[-1][-1]) + (len(nums)//2 - freq_odd[-2][-1]))
            
            
            elif (freq_even[-1][-1] > freq_odd[-1][-1] or freq_even[-1][-1] <= freq_odd[-1][-1])  and len(freq_even) > 1 and len(freq_odd) > 1 :
                return min((ceil(len(nums)/2) - freq_even[-2][-1]) + (len(nums)//2 - freq_odd[-1][-1]), (ceil(len(nums)/2) - freq_even[-1][-1]) + (len(nums)//2 - freq_odd[-2][-1]))
            elif freq_even[-1][-1] > freq_odd[-1][-1] and len(freq_odd) >= 2:
                return (ceil(len(nums)/2) - freq_even[-1][-1]) + (len(nums)//2 - freq_odd[-2][-1])
            
            elif (freq_even[-1][-1] > freq_odd[-1][-1] or freq_even[-1][-1] <= freq_odd[-1][-1])  and len(freq_even) > 1:
                return (ceil(len(nums)/2) - freq_even[-2][-1]) + (len(nums)//2 - freq_odd[-1][-1])
            else:
                return len(nums)//2