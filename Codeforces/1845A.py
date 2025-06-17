for _ in range(int(input())):
    n, k, x = list(map(int, input().split()))

    if x != 1:
        # can make with all 1s
        print("YES")
        print(n)
        for i in range(n - 1):
            print(1, end=' ')
        print(1)
    else:
        # x == 1
        # can only make with 2s and 3s
        if k == 1 or (k == 2 and n % 2 == 1):
            # can't use any ones or can't use 2s with odd n
            print("NO")
        else:
            # can be made with 2s and 3s
            print("YES")
            if n % 2 == 0:
                # even n, all 2s
                print(n // 2)
                for i in range(n // 2 - 1):
                    print(2, end=' ')
                print(2)
            else:
                # odd n, 2s followed by a 3
                print((n - 3) // 2 + 1)
                for i in range((n - 3) // 2):
                    print(2, end=' ')
                print(3)
