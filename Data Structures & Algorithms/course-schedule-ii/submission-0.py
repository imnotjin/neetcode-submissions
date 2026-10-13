class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegrees = {i: 0 for i in range(numCourses)}


        for course, pre in prerequisites:
            graph[pre].append(course)
            indegrees[course] += 1
        
        q = deque([course for course in indegrees if indegrees[course] == 0])
        print(q)
        res = []
        while q:
            course = q.popleft()
            res.append(course)

            for nei in graph[course]:
                indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    q.append(nei)
        
        return res if len(res) == numCourses else []
