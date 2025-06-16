import math


for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    diff = float("inf")
    for i in range(len(arr) - 1):
        d = arr[i + 1] - arr[i]
        diff = min(diff, d)

    if diff < 0:
        print(0)
    else:
        print(math.ceil((diff + 1) / 2))
