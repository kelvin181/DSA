for _ in range(int(input())):
    n, k = list(map(int, input().split()))

    if n % 2 == 1 and k % 2 == 0:
        print("NO")
    else:
        print("YES")
