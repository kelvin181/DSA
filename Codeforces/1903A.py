for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    if k <= 1:
        for i in range(1, n):
            if arr[i] < arr[i - 1]:
                print("NO")
                break
        else:
            print("YES")
    else:
        print("YES")
