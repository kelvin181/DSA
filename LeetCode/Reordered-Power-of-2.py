class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        # count digits and compare with possible powers of 2
        count = Counter(str(n))
        return any(count == Counter(str(1 << i)) for i in range(30))