class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        prev = []
        for i in range(len(skill)):
            if not prev:
                prev.append(skill[i] * mana[0])
            else:
                prev.append(prev[-1] + skill[i] * mana[0])

        def find(arr, num):
            res = arr[0]
            pre = num * skill[0]
            for i in range(1, len(skill)):
                if res + pre < arr[i]:
                    res = arr[i] - pre
                pre += num * skill[i]
            return res
        
        for i in range(1, len(mana)):
            start = find(prev, mana[i])
            prev = []
            for num in skill:
                if not prev:
                    prev.append(start + num * mana[i])
                else:
                    prev.append(prev[-1] + num * mana[i])
        
        return prev[-1]
