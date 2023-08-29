class Solution:
    def bestClosingTime(self, customers: str) -> int:
        
        n = len(customers)
        penality = [0 for _ in range(n + 1)]
        
        i = 0
        j = n - 1
        forward_penality = backward_penality = 0
        while i < n and j >= 0:
            
            penality[i] += forward_penality
            if customers[i] == "N":
                forward_penality += 1
            if customers[j] == "Y":
                backward_penality += 1
            penality[j] += backward_penality
            i += 1
            j -= 1
        penality[n] = forward_penality
        
        return penality.index(min(penality))