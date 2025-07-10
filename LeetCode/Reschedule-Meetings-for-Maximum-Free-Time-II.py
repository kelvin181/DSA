class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        res = 0
        right = eventTime
        post = deque([0])
        spaces = deque()

        for i in range(len(startTime) - 1, -1, -1):
            space = right - endTime[i]
            if not post:
                post.appendleft(space)
            else:
                post.appendleft(max(space, post[0]))
            spaces.appendleft(space)
            right = startTime[i]
        
        left = right
        pre_max = 0
        post_max = post.popleft()

        for i in range(len(startTime)):
            curr = endTime[i] - startTime[i]
            right = spaces.popleft()
            post_max = post[0]

            if post_max >= curr or pre_max >= curr:
                res = max(res, curr + left + right)
            else:
                res = max(res, left + right)
            
            pre_max = max(pre_max, left)
            left = right
            post.popleft()

        return res
