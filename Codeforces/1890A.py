for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    
    count = {}
    for num in arr:
        count[num] = count.get(num, 0) + 1
    
    if len(count) > 2:
        print("NO")
    else:
        if len(count) == 1:
            print("YES")
            continue
        key1, key2 = list(count.keys())
        if abs(count[key1] - count[key2]) > 1:
            print("NO")
        else:
            print("YES")
