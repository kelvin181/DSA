class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        user_langs = {i + 1: set(languages[i]) for i in range(len(languages))}
        friendships = [f for f in friendships if not user_langs[f[0]] & user_langs[f[1]]]

        if not friendships:
            return 0
        
        res = inf
        for lang in range(1, n + 1):
            teach = set()
            for a, b in friendships:
                if lang not in user_langs[a] and lang not in user_langs[b]:
                    teach.add(a)
                    teach.add(b)
                elif lang not in user_langs[a]:
                    teach.add(a)
                elif lang not in user_langs[b]:
                    teach.add(b)

            res = min(res, len(teach))

        return res
