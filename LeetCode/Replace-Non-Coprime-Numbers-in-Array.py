class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        s = []

        for num in nums:
            if s:
                top = s[-1]
                curr = num
                new = None
                while s and gcd(curr, top) > 1:
                    s.pop()
                    new = lcm(curr, top)
                    if s:
                        top = s[-1]
                        curr = new
                    else:
                        break
                if new:
                    s.append(new)
                else:
                    s.append(num)
            else:
                s.append(num)

        return s
