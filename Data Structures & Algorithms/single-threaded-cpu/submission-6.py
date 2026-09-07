class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        ext_tasks = sorted([(t[0], t[1], i) for i, t in enumerate(tasks)])

        res = []
        min_heap = []
        curr_time = 0
        i = 0
        n = len(tasks)

        while i < n or min_heap:
            if not min_heap and curr_time < ext_tasks[i][0]:
                curr_time = ext_tasks[i][0]
            
            while i < n and ext_tasks[i][0] <= curr_time:
                heapq.heappush(min_heap, (ext_tasks[i][1], ext_tasks[i][2]))
                i += 1

            proc_time, idx = heapq.heappop(min_heap)
            curr_time += proc_time
            res.append(idx)
            
        return res
