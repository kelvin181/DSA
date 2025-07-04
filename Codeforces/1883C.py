for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    
    res = k
    evens = 0
    for num in arr:
        if num % 2 == 0:
            evens += 1
        if num % k == 0:
            res = 0
        else:
            res = min(res, k - (num % k))
    
    if k == 4:
        if evens >= 2:
            res = 0
        elif evens == 1:
            res = min(res, 1)
        else:
            res = min(res, 2)
    
    print(res)
