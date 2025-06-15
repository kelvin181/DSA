class Solution:
    def maxDiff(self, num: int) -> int:
        num = str(num)
        biggest = inf
        smallest = inf

        for i in range(len(num)):
            if num[i] != '9':
                biggest = min(biggest, i)
            if num[i] != '0' and num[i] != '1':
                smallest = min(smallest, i)
        
        smallest_num = []
        biggest_num = []
        for i in range(len(num)):
            if biggest != inf and num[i] == num[biggest]:
                biggest_num.append("9")
            else:
                biggest_num.append(num[i])

            if smallest != inf and num[i] == num[smallest]:
                if smallest == 0:
                    smallest_num.append("1")
                else:
                    smallest_num.append("0")
            else:
                smallest_num.append(num[i])
        
        return int("".join(biggest_num)) - int("".join(smallest_num))
