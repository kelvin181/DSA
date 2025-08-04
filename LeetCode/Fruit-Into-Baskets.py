class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        res = 0
        l = 0
        seen = {}

        for i, num in enumerate(fruits):
            if num not in seen and len(seen) == 2:
                # O(1) because max 2 elements in seen
                l = min([seen[key] for key in seen]) + 1
                for key in seen:
                    if seen[key] == l - 1:
                        delete = key
                del seen[delete]

            seen[num] = i
            res = max(res, i + 1 - l)

        return res
