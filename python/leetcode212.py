from typing import List


class Trie:

    def __init__(self):
        self.children = {}
        self.isEnd = False
        self.word = ""

    def insert(self, word: str) -> None:
        cur = self
        for i in range(len(word)):
            if word[i] not in cur.children:
                cur.children[word[i]] = Trie()
            cur = cur.children[word[i]]
        cur.isEnd = True
        cur.word = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.board = board
        self.m, self.n = len(board), len(board[0])
        self.ans = set()
        self.root = Trie()
        for word in words:
            self.root.insert(word)

        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] in self.root.children:
                    self.dfs(i, j, 1, self.root)
        return list(self.ans)


    def dfs(self, i, j , cnt, node):
        cur_ch = self.board[i][j]
        if cur_ch not in node.children and cnt > 10:
            return
        _next = node.children[cur_ch]
        if _next.isEnd:
            self.ans.add(_next.word)
        self.board[i][j] = "#"
        for i_next, j_next in [[i + 1, j], [i, j + 1], [i - 1, j], [i, j - 1]]:
            if 0 <= i_next < self.m and 0 <= j_next < self.n:
                self.dfs(i_next, j_next, cnt + 1, _next)
        self.board[i][j] = cur_ch



if __name__ == '__main__':
    solution = Solution()
    board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
    words = ["oath","pea","eat","rain"]
    print(solution.findWords(board, words))