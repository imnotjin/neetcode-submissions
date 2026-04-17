class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        indegrees = defaultdict(int)
        outdegrees = defaultdict(int)

        for a, b in trust:
            outdegrees[a] += 1
            indegrees[b] += 1
        
        for k, v in indegrees.items():
            if v == n - 1 and outdegrees[k] == 0:
                return k
        
        return -1
