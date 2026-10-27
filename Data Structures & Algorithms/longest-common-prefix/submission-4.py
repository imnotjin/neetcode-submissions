class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = []
        for i in range(len(min(strs, key=len))):
            for j in range(1, len(strs)):
                print(strs[j][i], strs[j-1][i])
                if strs[j][i] != strs[j-1][i]:
                    return "".join(res)
            res.append(strs[0][i])
        
        return "".join(res)
