class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        que = deque([0])
        visited = set()
        while que:
            node = que.popleft()
            visited.add(node)
            
            for nei in rooms[node]:
                if nei not in visited:
                    que.append(nei)
        return len(visited) == len(rooms)