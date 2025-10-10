class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        # instead of placing boxes and finding closest houses to the box, 
        # group the houses into k groups 
        # within each group, find a place to place the box for min distance
        # store boxes left and index of house to start from as DP

        houses.sort()

        def get_cost(i, j):
            if i == j:
                return 0
            mid = (i + j) // 2
            res = 0
            for k in range(i, j + 1):
                res += abs(houses[k] - houses[mid])
            return res

        @cache 
        def dp(boxes, i):
            if boxes == 1:
                return get_cost(i, len(houses) - 1)

            res = inf
            for j in range(i, len(houses) - boxes + 1):
                cost = get_cost(i, j)
                res = min(res, dp(boxes - 1, j + 1) + cost)
            
            return res
        
        return dp(k, 0)
