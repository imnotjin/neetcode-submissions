class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = defaultdict(set)
        unique_letters = set()
        for word in words:
            for char in word:
                unique_letters.add(char)
        indegrees = {c: 0 for c in unique_letters}

        for i in range(len(words) - 1):
            left, right = words[i], words[i + 1]
            for j in range(len(left)):
                # left is longer than right
                if j >= len(right):
                    return ""

                # right is a prefix of left
                if left[j] == right[j]:
                    continue

                # update indegrees
                if right[j] not in adj[left[j]]:
                    indegrees[right[j]] += 1

                # update adj
                adj[left[j]].add(right[j])
                break
        

        q = deque([])
        for k, v in indegrees.items():
            if v == 0:
                q.append(k)
        
        print(q)
        ans = []

        while q:
            node = q.popleft()
            ans.append(node)

            for neighbor in adj[node]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    q.append(neighbor)
        

        return ''.join(ans) if len(ans) == len(unique_letters) else ""
