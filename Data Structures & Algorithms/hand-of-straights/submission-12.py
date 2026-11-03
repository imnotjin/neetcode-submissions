class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        count = Counter(hand)

        for x in sorted(count):
            need = count[x]
            if need == 0:
                continue
            
            for y in range(x, x + groupSize):
                if count[y] < need:
                    return False
                count[y] -= need
        
        return True