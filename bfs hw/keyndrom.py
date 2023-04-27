from typing import List

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = set()
        queue = [0]
        while queue:
            room = queue.pop(0)
            if room not in visited:
                visited.add(room)
                for key in rooms[room]:
                    if key not in visited:
                        queue.append(key)
        return len(visited) == n