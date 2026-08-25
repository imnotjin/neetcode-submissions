class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        indegrees = [0] * numCourses
        taken = 0

        for pre, c in prerequisites:
            adj[pre].append(c)
            indegrees[c] += 1
        
        q = deque([c for c in range(numCourses) if indegrees[c] == 0])

        while q:
            course = q.popleft()
            taken += 1

            for nei in adj[course]:
                indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    q.append(nei)
        
        return taken == numCourses
