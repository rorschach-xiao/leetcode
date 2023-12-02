from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant_q = deque()
        dire_q = deque()
        n = len(senate)
        for i, s in enumerate(senate):
            if s == 'R':
                radiant_q.append(i)
            else:
                dire_q.append(i)

        while radiant_q and dire_q:
            if dire_q[0] < radiant_q[0]:
                dire_q.append(dire_q[0] + n)
            else:
                radiant_q.append(radiant_q[0] + n)
            radiant_q.popleft()
            dire_q.popleft()
        return 'Radiant' if radiant_q else 'Dire'

if __name__ == '__main__':
    solution = Solution()
    print(solution.predictPartyVictory("DRDRDRDRRDRD"))