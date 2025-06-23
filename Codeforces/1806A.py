for _ in range(int(input())):
    x, y, x1, y1 = list(map(int, input().split()))

    res = 0

    up_moves = y1 - y
    if up_moves < 0:
        print(-1)
    else:
        right_moves = x1 - x
        if right_moves > up_moves:
            print(-1)
        else:
            print(up_moves + (x - x1 + up_moves))
