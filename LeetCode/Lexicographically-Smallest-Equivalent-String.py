class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        union = {chr(i + ord('a')): chr(i + ord('a')) for i in range(26)}

        def find(node):
            if union[node] == node:
                return node
            return find(union[node])
        
        for i in range(len(s1)):
            p1 = find(s1[i])
            p2 = find(s2[i])
            if p1 < p2:
                union[p2] = p1
            else:
                union[p1] = p2
        
        return "".join([find(char) for char in baseStr])
