for _ in range(int(input())):
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))
    
    prev = 0
    res = 0
    
    for i in range(len(arr)):
        res = max(res, arr[i] - prev)
        prev = arr[i]
    
    res = max(res, 2 * (x - prev))
    
    print(res)
