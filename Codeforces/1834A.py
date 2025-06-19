import math


for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    
    negative_count = sum(1 for num in arr if num < 0)
    target = math.floor(n / 2)

    res = max(0, negative_count - target)
    if (negative_count - res) % 2:
        res += 1

    print(res)
