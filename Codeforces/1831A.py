for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    res = [str(n + 1 - num) for num in arr]
    print(" ".join(res))
