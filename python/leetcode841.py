from collections import deque
from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visit = set()
        queue = deque()
        queue.append(0)
        while queue:
            cur_room = queue.popleft()
            visit.add(cur_room)
            keys = rooms[cur_room]
            for k in keys:
                if k not in visit:
                    queue.append(k)
        return len(visit) == len(rooms)