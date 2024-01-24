from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt = {}
        for task in tasks:
            if task not in cnt:
                cnt[task] = 1
            else:
                cnt[task] += 1
        maxCount = max(cnt.values())
        maxCountNum = 0
        for v in cnt.values():
            if v == maxCount:
                maxCountNum += 1

        return max((maxCount - 1) * (n + 1) + maxCountNum, len(tasks))