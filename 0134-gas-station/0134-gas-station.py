class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = 0
        cur_gas = gas[0]
        
        for i in range(2*len(gas) + 1):
            i %= len(gas)
            nex_idx = (i + 1)%len(gas)
            
            if start == nex_idx and cur_gas - cost[i] >= 0:
                return start
            
            if cur_gas > cost[i]:
                cur_gas =  cur_gas + gas[nex_idx] - cost[i]
            else:
                cur_gas = gas[nex_idx]
                start = nex_idx
                
        return -1