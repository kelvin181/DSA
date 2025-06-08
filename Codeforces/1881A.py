# operations will not exceed 5 because n * m < 25
# worst case is n = 1 and m = 25
# if we cannot find s in x after 5 operations, we will never be able to find it

for _ in range(int(input())):
    n, m = list(map(int, input().split()))
    x = input()
    s = input()
    
    res = -1
    curr = x
    for i in range(6):
        if s in curr:
            res = i
            break
        curr = curr + curr
    
    print(res)    
