class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = []
        
        while columnNumber > 0:
            columnNumber -= 1
            offset = columnNumber % 26
            ans.append(chr(ord('A') + offset))
            columnNumber //= 26

        return ''.join(reversed(ans))
