import math

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    
    g = math.gcd(*arr)
    
    if g == 1:
        print(0)
    elif math.gcd(g, n) == 1: # only n because g is the gcd of everything in arr, so gcd(g, n) is the same as gcd(g, gcd(arr[-1], n))
        print(1)
    elif math.gcd(g, n - 1) == 1: # same thing as above applies here 
        print(2)
    else: # we know if we perform the op on the last 2 indices, we can make gcd of arr 1. this is because gcd(n, n - 1) = 1
        print(3)
