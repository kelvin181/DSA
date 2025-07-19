class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        l = 0
        res = []
        
        for r in range(len(folder)):
            if folder[r][:len(folder[l]) + 1] == folder[l] + "/" or l == r:
                continue
            res.append(folder[l])
            l = r
            
        res.append(folder[l])
        return res
