class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()

        @cache
        def search(val):
            l = 0
            r = len(potions) - 1
            res = inf

            while l <= r:
                m = l + (r - l) // 2
                if potions[m] * val >= success:
                    res = min(res, m)
                    r = m - 1
                else:
                    l = m + 1
            
            if res == inf:
                return 0
            return len(potions) - res
                
        return [search(spell) for spell in spells]
