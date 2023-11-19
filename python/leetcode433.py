class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def isAdj(word1, word2):
            diff = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    diff += 1
                if diff > 1:
                    break
            return diff == 1

        if endWord not in wordList:
            return 0
        if isAdj(beginWord, endWord):
            return 2

        edges = {beginWord: []}
        visit = {beginWord: False}
        n = len(wordList)
        # construct directed graph
        for i in range(n):
            visit[wordList[i]] = False
            if isAdj(beginWord, wordList[i]):
                edges[beginWord].append(wordList[i])
            for j in range(i + 1, n):
                if isAdj(wordList[i], wordList[j]):
                    if wordList[i] not in edges:
                        edges[wordList[i]] = [wordList[j]]
                    else:
                        edges[wordList[i]].append(wordList[j])
                    if wordList[j] not in edges:
                        edges[wordList[j]] = [wordList[i]]
                    else:
                        edges[wordList[j]].append(wordList[i])

        # BFS
        queue = [(beginWord, 1)]
        while len(queue) > 0:
            cur = queue.pop(0)
            if cur[0] not in edges:
                continue
            for next_word in edges[cur[0]]:
                if next_word == endWord:
                    return cur[1] + 1
                if not visit[next_word]:
                    visit[next_word] = True
                    queue.append((next_word, cur[1] + 1))
        return 0