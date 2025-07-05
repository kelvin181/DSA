class Solution:
    def minSwaps(self, s: str) -> int:

        def count_mismatches(s, first_letter):
            count = 0
            for i in range(len(s)):
                if i % 2 == 0 and s[i] != first_letter:
                    count += 1
            return count
            
        length = len(s)
        
        counter = Counter(s)
        
        # impossible
        if abs(counter.get("1", 0) - counter.get("0", 0)) > 1:
            return -1

        # empty string
        if length <= 1:
            return 0

        res = float('inf')
        
        if length % 2 == 0:
            # start with any
            # check start with 0
            res = min(res, count_mismatches(s, "0"))
            
            # check start with 1
            res = min(res, count_mismatches(s, "1"))
        else:
            # start with the more
            if counter.get("1", 0) > counter.get("0", 0):
                res = min(res, count_mismatches(s, "1"))
            else:
                res = min(res, count_mismatches(s, "0"))
        
        return res
