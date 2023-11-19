from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        word2id = {beginWord: 1}
        edges = {1: []}
        visit = {1: False}
        cnt = 1
        def addWord(word):
            nonlocal cnt
            if word not in word2id:
                cnt += 1
                word2id[word] = cnt
                visit[cnt] = False


        def addEdge(word):
            addWord(word)
            id = word2id[word]
            chars = list(word)
            for i in range(len(chars)):
                tmp = chars[i]
                chars[i] = "*"
                newWord = "".join(chars)
                addWord(newWord)
                newId = word2id[newWord]
                if id in edges:
                    edges[id].append(newId)
                else:
                    edges[id] = [newId]
                if newId in edges:
                    edges[newId].append(id)
                else:
                    edges[newId] = [id]
                chars[i] = tmp

        for word in wordList:
            addEdge(word)
        addEdge(beginWord)

        # BFS
        queue = [(word2id(beginWord), 1)]
        while len(queue) > 0:
            cur = queue.pop(0)
            for next_word in edges[cur[0]]:
                if next_word == word2id[endWord]:
                    return cur[1] // 2 + 1
                if not visit[next_word]:
                    visit[next_word] = True
                    queue.append((next_word, cur[1] + 1))
        return 0