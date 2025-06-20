for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    res = 0
    l = 0
    for r in range(n):
        if arr[r] == 1:
            res = max(res, r - l)
            l = r + 1
    res = max(res, n - l)
    print(res)
