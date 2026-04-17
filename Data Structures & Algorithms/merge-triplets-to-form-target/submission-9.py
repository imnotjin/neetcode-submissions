class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        n = len(triplets)

        def bfs(i):
            q = deque([triplets[i]])
            v = set()
            v.add(tuple(triplets[i]))

            while q:
                print(q)
                a, b, c = q.popleft()
                
                if a > target[0] or b > target[1] or c > target[2]:
                    continue
                
                if [a, b, c] == target:
                    return True

                for nei in triplets + list(q):
                    if tuple(nei) not in v:
                        q.append([max(a, nei[0]), max(b, nei[1]), max(c, nei[2])])
                        v.add(tuple(nei))

        for i in range(n):
            print(f"starting {i}")
            if bfs(i):
                return True
            print(f"ending {i}")
        return False