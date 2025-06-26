for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    
    # if we xor x with itself, it becomes 0
    # for every num in arr, we xor it with x
    # therefore, if n is even, xoring x with itself n times will result in 0
    # if n is odd, we end up with the value of x. 
    # this means that we can just xor the xor of the arr with itself to get 0
    # if n is even, we can only get 0 if the xor of the arr is 0
    
    total = 0
    for num in arr:
        total ^= num
        
    if n % 2:
        print(total)
    else:
        if total == 0:
            print(0)
        else:
            print(-1)
