class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []
        m, n = len(word1), len(word2)
        i = j = 0
        while i < m and j < n:
            merged.append(word1[i])
            merged.append(word2[j])
            i += 1
            j += 1
        
        if m > n:
            merged.append(word1[i:])
        if m < n:
            merged.append(word2[j:])
        
        return "".join(merged)
