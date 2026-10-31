class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for w in words for c in w}
        idg = {c: 0 for c in adj}
        n = len(words)

        for i in range(1, n):
            a, b = words[i-1], words[i]
            min_len = min(len(a), len(b))
            if len(a) > len(b) and a[:min_len] == b[:min_len]:
                return ""
            for j in range(min_len):
                if a[j] != b[j]:
                    if b[j] not in adj[a[j]]:
                        adj[a[j]].add(b[j])
                        idg[b[j]] += 1
                    break
        
        res = []
        q = deque([c for c in idg if idg[c] == 0])
        while q:
            c = q.popleft()
            res.append(c)
            for nei in adj[c]:
                idg[nei] -= 1
                if idg[nei] == 0:
                    q.append(nei)

        return "".join(res) if len(res) == len(idg) else ""

