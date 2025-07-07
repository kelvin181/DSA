class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        q = deque([id])
        visited = set([id])
        
        while q and level > 0:
            for _ in range(len(q)):
                curr = q.popleft()
                for friend in friends[curr]:
                    if friend not in visited:
                        visited.add(friend)
                        q.append(friend)
            level -= 1
        
        counter = {}
        for person in q:
            for video in watchedVideos[person]:
                counter[video] = counter.get(video, 0) + 1
        
        return [item[0] for item in sorted(counter.items(), key=lambda x:(x[1], x[0]))]
