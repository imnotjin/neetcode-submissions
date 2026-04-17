class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0] * 26
        for task in tasks:
            freq[ord(task) - ord('A')] += 1
        freq.sort()
        max_f = freq[25]
        idle = (max_f - 1) * n
        
        for i in range(24, -1, -1):
            idle -= min(max_f - 1, freq[i])
        
        return max(0, idle) + len(tasks)
