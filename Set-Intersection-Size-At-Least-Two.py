class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        """
        track the last 2 values added
        sort by asc end and desc start
        if two intervals have the same end, we want to choose the highest 
        vals to accommodate all intervals
        """

        intervals.sort(key = lambda p:(p[1], -p[0]))
        res = 0
        pre = []

        for a, b in intervals:
            if not pre or pre[1] < a:
                # no overlap with pre, choose 2 biggest vals
                pre = [b - 1, b]
                res += 2
            elif pre[0] < a:
                # single overlap with pre, choose max(pre) and max(a, b)
                pre = [pre[1], b]
                res += 1
            # else: fully overlap, no need to add
        
        return res
