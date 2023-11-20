class WordDictionary:

    def __init__(self):
        self.root = Trie()

    def addWord(self, word: str) -> None:
        self.root.insert(word)

    def dfs(self, word, index, node):
        if index >= len(word):
            return node.isEnd
        re = False
        if word[index] == '.':
            for i in range(26):
                if node.children[i]:
                    re = self.dfs(word, index + 1, node.children[i])
                if re:
                    return True
        else:
            ch = ord(word[index]) - ord('a')
            if node.children[ch] is None:
                return False
            re = self.dfs(word, index + 1, node.children[ch])
        return re

    def search(self, word: str) -> bool:
        return self.dfs(word, 0, self.root)


class Trie:

    def __init__(self):
        self.children = [None for _ in range(26)]
        self.isEnd = False

    def insert(self, word: str) -> None:
        cur = self
        for i in range(len(word)):
            ch = ord(word[i]) - ord('a')
            if cur.children[ch] is None:
                cur.children[ch] = Trie()
            cur = cur.children[ch]
        cur.isEnd = True

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)