class Solution:
    def clearStars(self, s: str) -> str:
        # O(n) with slower runtime than heap approach
        count = {chr(ord('a') + i): [] for i in range(26)}
        arr = list(s)

        for i, char in enumerate(s):
            if char == "*":
                for j in range(26):
                    if count[chr(ord('a') + j)]:
                        index = count[chr(ord('a') + j)].pop()
                        arr[index] = ""
                        break
            else:
                count[char].append(i)
        
        res = []
        for char in arr:
            if char != "*":
                res.append(char)
        
        return "".join(res)

        # O(nlogn) using heap that has a faster runtime on given test cases
        
        # heap = []
        # deleted = set()

        # for i, char in enumerate(s):
        #     if char != "*":
        #         heappush(heap, (char, -i))
        #     else:
        #         char, index = heappop(heap)
        #         deleted.add(-index)
        
        # res = []
        # for i, char in enumerate(s):
        #     if i not in deleted and char != "*":
        #         res.append(char)
        
        # return "".join(res)
