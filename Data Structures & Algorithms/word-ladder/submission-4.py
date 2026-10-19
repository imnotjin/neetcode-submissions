class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0
        
        res = 1
        v = {beginWord}
        q = deque([beginWord])
        while q:
            q_len = len(q)
            for _ in range(q_len):
                word = q.popleft()
                if word == endWord:
                    return res
                for i in range(len(word)):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        new_word = word[:i] + c + word[i+1:]
                        if new_word not in v and new_word in word_set:
                            v.add(new_word)
                            q.append(new_word)
            res += 1
        return 0
