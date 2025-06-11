for _ in range(int(input())):
    score = 0
    
    for x in range(10):
        row = input()
        for y in range(10):
            if row[y] == 'X':
                if x == 0 or x == 9 or y == 0 or y == 9:
                    score += 1
                elif x == 1 or x == 8 or y == 1 or y == 8:
                    score += 2
                elif x == 2 or x == 7 or y == 2 or y == 7:
                    score += 3
                elif x == 3 or x == 6 or y == 3 or y == 6:
                    score += 4
                else:
                    score += 5
        
    print(score)
