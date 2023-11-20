class Trie:

    def __init__(self):
        self.children = [None for _ in range(26)]
        self.isEnd = False

    def __searchPrefix(self, prefix):
        cur = self
        for i in range(len(prefix)):
            ch = ord(prefix[i]) - ord('a')
            if cur.children[ch] is None:
                return None
            cur = cur.children[ch]
        return cur

    def insert(self, word: str) -> None:
        cur = self
        for i in range(len(word)):
            ch = ord(word[i]) - ord('a')
            if cur.children[ch] is None:
                cur.children[ch] = Trie()
            cur = cur.children[ch]
        cur.isEnd = True

    def search(self, word: str) -> bool:
        re = self.__searchPrefix(word)
        if re is None:
            return False
        return re.isEnd

    def startsWith(self, prefix: str) -> bool:
        re = self.__searchPrefix(prefix)
        if re is None:
            return False
        return True
