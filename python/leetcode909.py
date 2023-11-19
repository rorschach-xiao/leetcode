class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        def id2rc(label, n):
            r = (label - 1) // n
            if r % 2 == 1:
                c = (n - 1)- (label - 1) % n
            else:
                c = (label - 1) % n
            return (n- 1 - r, c)
        n = len(board)
        if n == 0:
            return 0
        visit = [False for _ in range(n ** 2 + 1)]
        queue = [(1, 0)]
        while len(queue) > 0:
            cur = queue.pop(0)
            visit[cur[0]] = True
            for i in range(1, 7):
                next_label = cur[0] + i
                if next_label > n ** 2:
                    break
                r, c = id2rc(next_label, n)
                if board[r][c] > -1:
                    next_label = board[r][c]
                if next_label == n ** 2:
                    return cur[1] + 1
                if not visit[next_label]:
                    visit[next_label] = True
                    queue.append((next_label, cur[1] + 1))

        return  -1