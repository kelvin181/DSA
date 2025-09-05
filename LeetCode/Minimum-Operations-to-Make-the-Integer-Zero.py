class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        # num1 - x * num2. find x power of 2s that sum to that 

        x = 1
        while True:
            target = num1 - num2 * x
            if target < x:
                return -1
            if x >= target.bit_count(): # can always split it up. e.g. 2 * 4 instead of 8
                return x
            x += 1
