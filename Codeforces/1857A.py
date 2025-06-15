for _ in range(int(input())):
    t = int(input())
    arr = list(map(int, input().split()))

    if sum(arr) % 2:
        print("NO")
    else:
        if len(arr) > 1:
            print("YES")
        else:
            print("NO")
