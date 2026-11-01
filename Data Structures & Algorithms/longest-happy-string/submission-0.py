class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = [
            (-cnt, ch) for cnt, ch in [(a, 'a'), (b, 'b'), (c, 'c')] if cnt > 0
        ]
        heapq.heapify(heap)

        res = []
        while heap:
            cnt, ch = heapq.heappop(heap)
            if len(res) >= 2 and res[-2] == res[-1] == ch:
                if not heap:
                    break
                cnt2, ch2 = heapq.heappop(heap)
                res.append(ch2)
                if cnt2 + 1 < 0:
                    heapq.heappush(heap, (cnt2 + 1, ch2))
                heapq.heappush(heap, (cnt, ch))
            else:
                res.append(ch)
                if cnt + 1 < 0:
                    heapq.heappush(heap, (cnt + 1, ch))
        return "".join(res)