class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        count = {"N": 0, "S": 0, "E": 0, "W": 0}

        res = 0

        for char in s:
            count[char] += 1
            miny = min(count["N"], count["S"])
            minx = min(count["E"], count["W"])
            maxy = max(count["N"], count["S"])
            maxx = max(count["E"], count["W"])
            opp = miny + minx

            res = max(res, (maxy - miny) + (maxx - minx) + min(opp, k) * 2)

        return res
