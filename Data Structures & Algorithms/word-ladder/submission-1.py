class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0

        ans = 1

        q = deque([(beginWord, ans)])
        v = set()
        v.add(beginWord)

        while q:
            word, ans = q.popleft()

            if word == endWord:
                return ans

            for i, c in enumerate(word):
                for x in "abcdefghijklmnopqrstuvwxyz":
                    new_word = word[:i] + x + word[i+1:]
                    # print(new_word)

                    if new_word not in v and new_word in word_set:
                        q.append((new_word, ans + 1))
                        v.add(new_word)
        
        return 0



        

