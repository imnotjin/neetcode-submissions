class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        ans = 0
        seen = set()

        def dfs(s_idx, t_idx, word):
            nonlocal ans
            if tuple(word) in seen:
                return

            if t_idx == len(t):
                seen.add(tuple(word))
                ans += 1
                return
            
            if s_idx == len(s):
                return
            
            if s[s_idx] == t[t_idx]:
                word.append(s_idx)
                while s_idx < len(s):
                    s_idx += 1
                    dfs(s_idx, t_idx + 1, word)
                word.pop()
            else:
                dfs(s_idx + 1, t_idx, word)
        
        for i in range(len(s)):
            dfs(i, 0, [])
        print(seen)
        return ans

        # caaat cat
        #     aaat at
        #         aat t
        #         aat t    
        #     aaat at
        #         aat t
        #         aat t
        #     aaat at
        #         aat t
        #         aat t
