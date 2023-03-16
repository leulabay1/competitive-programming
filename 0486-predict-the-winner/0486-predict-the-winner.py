class Solution:
    
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def predict(i, j, player1):
            if i > j:
                return 0, 0
            
            else:
                p1l, p2l = predict(i+1, j, not player1)
                
                p1r, p2r = predict(i, j-1, not player1)
                
                if player1:
                    p1l += nums[i]
                    p1r += nums[j]
                    if p1l > p1r:
                        return p1l, p2l
                    else:
                        return p1r, p2r
                else:
                    p2l += nums[i]
                    p2r += nums[j]
                    if p2l > p2r:
                        return p1l, p2l
                    else:
                        return p1r, p2r
        p1, p2 = predict(0, len(nums)-1, True)
        return p1 >= p2