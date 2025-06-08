class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, num):
        num = str(num)
        curr = self.root

        for digit in num:
            digit = int(digit)
            if digit in curr.children:
                curr = curr.children[digit]
            else:
                curr.children[digit] = TrieNode(digit)
                curr = curr.children[digit]

        curr.end = True    


class TrieNode:
    def __init__(self, val=-1):
        self.end = False
        self.val = val
        self.children = {}


class Solution:
    def lexicalOrder(self, n: int) -> list[int]:
        \\\
        Faster solution
        \\\
        res = []
        curr = 1

        for _ in range(n):
            res.append(curr)

            if curr * 10 <= n:
                # always add a 0 first if you can
                curr *= 10
            else:
                # backtrack to find the next lexicographically smallest number
                if curr >= n:
                    curr //= 10
                curr += 1
                while curr % 10 == 0:
                    curr //= 10

        return res

        \\\
        Slower solution using a trie
        \\\
        # trie = Trie()
        # for i in range(1, n + 1):
        #     trie.insert(i)
        
        # curr = []
        # res = []
        # digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        # def dfs(node):
        #     if len(curr) > len(str(n)):
        #         return
            
        #     if node.end:
        #         res.append(self.arr_to_int(curr))
            
        #     for digit in digits:
        #         if digit in node.children:
        #             curr.append(digit)
        #             dfs(node.children[digit])
        #             curr.pop()  

        # dfs(trie.root)
        # return res

    def arr_to_int(self, arr):
        res = 0
        multi = 1
        for i in range(len(arr) - 1, -1, -1):
            res += arr[i] * multi
            multi *= 10
        return res