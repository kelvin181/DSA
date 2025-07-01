from typing import Counter


for _ in range(int(input())):
    s = input()
    
    t = []
    
    for i in range(len(s)):
        if s[i] == '1':
            t.append('0')
        else:
            t.append('1')
    
    i = 0
    count = Counter(s)
    
    for j in range(len(s)):
        if t[i] == "1":
            if count["1"] > 0:
                count["1"] -= 1
                i += 1
        else:
            if count["0"] > 0:
                count["0"] -= 1
                i += 1
    
    print(len(s) - i)
        