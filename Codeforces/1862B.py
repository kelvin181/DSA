for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    
    res = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] < res[-1]:
            res.append(1)
        res.append(arr[i])
    
    print(len(res))
    print(" ".join([str(num) for num in res]))
