class Solution:
    def maximumGain(self, st: str, x: int, y: int) -> int:
        res = 0
        stack1 = []

        for char in st:
            if char != "a" and char != "b":
                stack1.append(char)
                continue

            if x > y:
                if stack1 and stack1[-1] == "a" and char == "b":
                    res += x
                    stack1.pop()
                else:
                    stack1.append(char)
            else:
                if stack1 and stack1[-1] == "b" and char == "a":
                    res += y
                    stack1.pop()
                else:
                    stack1.append(char)

        stack2 = []
        for char in stack1:
            if char != "a" and char != "b":
                stack2.append(char)
                continue
                
            if char == "b":
                if stack2 and stack2[-1] == "a":
                    res += x
                    stack2.pop()
                else:
                    stack2.append(char)
            else: 
                if stack2 and stack2[-1] == "b":
                    res += y
                    stack2.pop()
                else:
                    stack2.append(char)
        
        return res
