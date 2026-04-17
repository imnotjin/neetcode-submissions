class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        R, D = deque(), deque()
        n = len(senate)

        for i, s in enumerate(senate):
            if s == "R":
                R.append(i)
            else:
                D.append(i)
        
        while D and R:
            dTurn = D.popleft()
            rTurn = R.popleft()

            if rTurn < dTurn:
                R.append(rTurn + n)
            else:
                D.append(dTurn + n)
        
        return "Radiant" if R else "Dire"
