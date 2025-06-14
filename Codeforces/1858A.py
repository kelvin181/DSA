for _ in range(int(input())):
    a, b, c = list(map(int, input().split()))

    if c % 2 == 0:
        if a > b:
            print("First")
        else:
            print("Second")
    else:
        if a > b - 1:
            print("First")
        else:
            print("Second")
