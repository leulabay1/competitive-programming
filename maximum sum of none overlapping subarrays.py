def maxSumTwoNoOverlap(self, nums: List[int], FirstLen: int, SecondLen: int) -> int:
        fast = rp = slow = lp = 0
        sum1 = 0
        
        firstLen= max(FirstLen, SecondLen)
        secondLen= min(FirstLen, SecondLen)
        while fast < len(nums):
            if fast - slow +1 < firstLen:
                fast += 1
            if fast - slow +1 == firstLen:
                
                if sum(nums[slow:fast+1]) > sum1:
                    sum1 = sum(nums[slow:fast+1])
                    rp = fast
                    lp = slow
                slow += 1
                fast += 1
                    
        
        fast = slow = 0
        sum2 = 0
        while fast < len(nums):
            if fast == lp:
                slow = fast = rp+1
            if fast - slow + 1 < secondLen:
                fast += 1
                continue
            if fast - slow + 1 == secondLen:
                sum2 = max(sum(nums[slow:fast+1]), sum2)
                slow += 1
                fast += 1
        print(sum1, sum2)
        SumFirst = sum1+sum2
        
#-------------------------------------------------------------------------------
        
        fast = rp = slow = lp = 0
        sum3 = 0
        firstLen=min(FirstLen,SecondLen)
        secondLen=max(FirstLen,SecondLen)
        while fast < len(nums):
            if fast - slow +1 < firstLen:
                fast += 1
            if fast - slow +1 == firstLen:
                
                if sum(nums[slow:fast+1]) > sum3:
                    sum3 = sum(nums[slow:fast+1])
                    rp = fast
                    lp = slow
                slow += 1
                fast += 1
                    
        fast = slow = 0
        sum4 = 0
        while fast < len(nums):
            if fast == lp:
                slow = fast = rp+1
            if fast - slow + 1 < secondLen:
                fast += 1
                continue
            if fast - slow + 1 == secondLen:
                sum4 = max(sum(nums[slow:fast+1]), sum4)
                slow += 1
                fast += 1
        print(sum3, sum4)
        SumSecond = sum3+sum4
        print(SumFirst, SumSecond)
        return max(SumFirst, SumSecond)
