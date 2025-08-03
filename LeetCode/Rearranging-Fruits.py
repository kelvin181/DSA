class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        count1 = Counter(basket1)
        count2 = Counter(basket2)
        all_keys = set(count1.keys()).union(count2.keys())

        swaps = {}
        target = 0
        min_key = inf

        for key in all_keys:
            total = count1.get(key, 0) + count2.get(key, 0)
            if total % 2:
                return -1
            if count1.get(key, 0) != total // 2:
                swaps[key] = abs(total // 2 - count1.get(key, 0))
                target += swaps[key]
            min_key = min(min_key, key)

        target //= 2
        swaps = sorted(swaps.items())
        index = 0
        res = 0

        while target > 0:
            val, count = swaps[index]
            if count >= target:
                res += min(target * val, min_key * target * 2)
                break
            else:
                res += min(count * val, min_key * count * 2)
                target -= count
                index += 1
        
        return res
