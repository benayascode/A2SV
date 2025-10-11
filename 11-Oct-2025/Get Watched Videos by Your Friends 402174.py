# Problem: Get Watched Videos by Your Friends - https://leetcode.com/problems/get-watched-videos-by-your-friends/description/

class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        arr = defaultdict(int)
        q = deque([id])
        visited = set([id])

        while level > 0:
            for _ in range(len(q)):
                x = q.popleft()

                for i in friends[x]:
                    if i not in visited:
                        visited.add(i)
                        q.append(i)

                        if level == 1:
                            for vid in watchedVideos[i]:
                                arr[vid] += 1
            
            level -= 1

        return sorted(list(arr.keys()), key = lambda k: (arr[k], k))