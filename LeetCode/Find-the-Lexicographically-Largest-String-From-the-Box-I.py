class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word

        target_char = max(list(word))
        max_length = len(word) - (numFriends - 1)
        res = ""

        for i in range(len(word)):
            if word[i] == target_char:
                res = max(res, word[i: i + max_length])
        
        return res
