class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        if len(senate) == 1:
            return "Radiant" if senate[0] == 'R' else "Dire"

        count = Counter(senate)
        q = deque([])
        for s in senate:
            q.append(s)
        
        while q:

            s = q.popleft()

            if s == "Ban":
                continue

            if s == 'R':
                for i in range(len(q)):
                    if q[i] == 'D':
                        q[i] = "Ban"
                        count['D'] -= 1
                        if count['D'] == 0:
                            return "Radiant"
                        break
            else:
                for i in range(len(q)):
                    print(i)
                    if q[i] == 'R':
                        q[i] = "Ban"
                        count['R'] -= 1
                        if count['R'] == 0:
                            return "Dire"
                        break

            q.append(s)                        
        
        return ""
