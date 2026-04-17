class Solution:
    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            str_len = int(s[i:j])
            strs.append(s[j + 1: j + 1 + str_len])
            i = j + 1 + str_len
        return strs
