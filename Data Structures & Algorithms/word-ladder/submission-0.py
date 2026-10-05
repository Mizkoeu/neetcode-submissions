class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0
        pattern_map = defaultdict(list)
        l = len(beginWord)
        for w in wordList:
            for i in range(l):
                pattern = w[:i] + '*' + w[i+1:]
                pattern_map[pattern].append(w)
        # begin BFS
        q = deque([(beginWord, 1)])
        visited = set([beginWord])
        while q:
            w, step = q.popleft()
            for i in range(l):
                pattern = w[:i] + '*' + w[i+1:]
                neighbors = pattern_map[pattern]
                for neighbor in neighbors:
                    if neighbor == endWord:
                        return step+1
                    if neighbor not in visited:
                        visited.add(neighbor)
                        q.append((neighbor, step+1))
        return 0

        
        