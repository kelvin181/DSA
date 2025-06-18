for _ in range(int(input())):
    x, k = list(map(int, input().split()))
    
    if x % k == 0:
        print(2)
        print(1, x - 1)
    else:
        print(1)
        print(x)