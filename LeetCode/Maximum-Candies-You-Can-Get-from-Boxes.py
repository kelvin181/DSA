class Solution:
    def reverseParentheses(self, s):
        stack = []
        opens = []

        for char in s:
            if char == \(\:
                opens.append(len(stack))
            elif char == \)\:
                start = opens.pop()
                stack[start:] = stack[start:][::-1]
            else:
                stack.append(char)
        
        return \\.join(stack)