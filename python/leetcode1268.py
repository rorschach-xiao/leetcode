class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trieRoot = Trie()
        for product in products:
            trieRoot.insert(product)
        n = len(searchWord)
        ans = []
        node = trieRoot
        for i in range(n):
            node = trieRoot.searchPrefix(searchWord[i], node)
            ans.append(trieRoot.recommand(searchWord[:i + 1], node))
        return ans


class Trie:
    def __init__(self):
        self.children = [None for i in range(26)]
        self.isEnd = False
        self.word = ''

    def insert(self, word):
        n = len(word)
        cur_node = self
        for i in range(n):
            ch = ord(word[i]) - ord('a')
            if cur_node.children[ch] is None:
                cur_node.children[ch] = Trie()
            cur_node = cur_node.children[ch]
        cur_node.isEnd = True
        cur_node.word = word

    def recommand(self, prefix, node):
        def dfs(node):
            nonlocal res
            if len(res) == 3:
                return
            if node.isEnd:
                res.append(node.word)

            for i in range(26):
                if node.children[i] is not None:
                    dfs(node.children[i])
                if len(res) == 3:
                    return

        res = []
        if node is not None:
            dfs(prefix, node)
        return res

    def searchPrefix(self, prefix, node):
        n = len(prefix)
        if not node:
            return None
        cur_node = node
        for i in range(n):
            ch = ord(prefix[i]) - ord('a')
            if cur_node.children[ch] is None:
                return None
            cur_node = cur_node.children[ch]
        return cur_node