class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        
        @cache
        def find(start, end):
            if start + 2 > end:
                return 0
            
            if start + 2 == end:
                return values[start] * values[start + 1] * values[start + 2]
            
            return min(values[start] * values[mid] * values[end] + find(start, mid) + find(mid, end) for mid in range(start + 1, end))

        return find(0, len(values) - 1)
