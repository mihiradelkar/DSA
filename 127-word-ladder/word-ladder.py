class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        word_map = defaultdict(list)
        for word in [beginWord] + wordList:
            for i in range(len(word)):
                pattern = word[:i]+"*"+word[i+1:]
                word_map[pattern].append(word)
        # print(word_map)
        queue = deque([(beginWord,1)])
        visited = {beginWord}
        jumps = 0
        while queue:
            word, jump = queue.popleft()
            if word == endWord:
                return jump
            for i in range(len(word)):
                pattern = word[:i]+"*"+word[i+1:]
                for neighbor in word_map[pattern]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor,jump+1))
        return 0        