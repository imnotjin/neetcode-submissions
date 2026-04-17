class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        start = net = 0
        
        for i, g in enumerate(gas):
            net += g - cost[i]
            
            if net < 0:
                net = 0
                start = i + 1
                
             
        return start
