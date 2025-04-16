# Problem: Keys and Rooms - https://leetcode.com/problems/keys-and-rooms/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        arr = deque([0])
        visited = [0 for i in range(len(rooms))]

        while arr:
            n = arr.popleft()
            if visited[n] == 0:
                visited[n] = 1
                for i in rooms[n]:
                    arr.append(i)
        
        for i in visited:
            if i == 0:
                return False
        return True