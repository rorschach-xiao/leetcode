class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        d = 'L' + dominoes + 'R'
        res = []
        l = 0
        for r in range(1, len(d)):
            if d[r] == '.':
                continue
            mid = r - l - 1
            if l != 0:
                res.append(d[l])
            if d[r] == d[l]:
                res.append(d[l] * mid)
            elif d[r] == 'R' and d[l] == 'L':
                res.append('.' * mid)
            else:
                res.append('R'* (mid // 2) + '.' * (mid % 2) + 'L' * (mid // 2))
            l = r
        return ''.join(res)