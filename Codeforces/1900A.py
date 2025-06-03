for _ in range(int(input())):
    n = map(int, input().split())
    s = input()
    spaces = [len(space) for space in s.split("#")]
    
    if max(spaces) >= 3:
        print(2)
    else:
        print(sum(spaces))
