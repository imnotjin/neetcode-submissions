class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        combs = []
        comb = []
        digits_dict = {2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}

        def bt(i):
            if len(comb) == len(digits):
                if comb:
                    combs.append("".join(comb))
                return
            
            for letter in digits_dict[int(digits[i])]:
                comb.append(letter)
                bt(i + 1)
                comb.pop()
        
        bt(0)
        return combs
