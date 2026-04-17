class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, t in enumerate(tasks):
            t.append(i)

        tasks.sort()
        ans = []
        min_heap = []
        
        curr_t = 1
        i = 0
        print(tasks)
        while min_heap or i < len(tasks):
            while i < len(tasks) and tasks[i][0] <= curr_t:
                heapq.heappush(min_heap, (tasks[i][1], tasks[i][2]))
                i += 1
            if min_heap:
                proc_t, idx = heapq.heappop(min_heap)
                ans.append(idx)
                curr_t += proc_t
            else:
                curr_t = tasks[i][0] + tasks[i][1]
                ans.append(tasks[i][2])
                i += 1
        
        return ans
