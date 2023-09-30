class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        num=str(n)
        leng=len(num)
        prev=0
        ans=""
        for i in range(1,leng+1):
            if i==leng:
                while prev<leng:
                    ans+=str(num[prev])
                    prev+=1
                return int(ans)
            elif num[prev]==num[i]:continue
            elif num[prev]<num[i]:
                while prev<i:
                    ans+=num[prev]
                    prev+=1
            else:
                ans+=str(int(num[prev])-1)
                ans+='9'*(leng-len(ans))
                return int(ans)