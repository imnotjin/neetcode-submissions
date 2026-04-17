class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = [set() for _ in range(numCourses)]
        isPreReq = [set() for _ in range(numCourses)]
        indegrees = [0] * numCourses

        for pre, course in prerequisites:
            adj[pre].add(course)
            indegrees[course] += 1

        q = deque([i for i in range(numCourses) if indegrees[i] == 0])

        while q:
            node = q.popleft()
            for neighbor in adj[node]:
                # direct
                isPreReq[neighbor].add(node)
                # indirect
                isPreReq[neighbor].update(isPreReq[node])
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    q.append(neighbor)

        return [u in isPreReq[v] for u, v in queries]