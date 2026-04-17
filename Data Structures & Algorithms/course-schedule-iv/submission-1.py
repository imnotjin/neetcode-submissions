class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = [set() for _ in range(numCourses)]
        is_prereq = [set() for _ in range(numCourses)]
        indegrees = [0] * numCourses

        for pre, crs in prerequisites:
            adj[pre].add(crs)
            indegrees[crs] += 1
        
        q = deque([i for i in range(numCourses) if indegrees[i] == 0])

        while q:
            node = q.popleft()

            for neighbor in adj[node]:
                is_prereq[neighbor].add(node)
                is_prereq[neighbor].update(is_prereq[node])
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    q.append(neighbor)

        return [u in is_prereq[v] for u, v in queries]