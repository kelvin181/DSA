for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    res = [0] * n
    prev = [-1] * n
    
    for i, num in enumerate(arr):
        if prev[num - 1] == -1 or (i - prev[num - 1] - 1) % 2 == 0:
            res[num - 1] += 1
        prev[num - 1] = i

    print(" ".join([str(num) for num in res]))
