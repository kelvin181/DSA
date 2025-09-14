class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        
        def remove_vowels(word):
            return "".join("*" if char in "aeiou" else char for char in word)
        
        words = set(wordlist)
        words_lower = {}
        words_vowels_removed = {}

        for word in wordlist[::-1]:
            lower = word.lower()
            words_lower[lower] = word
            words_vowels_removed[remove_vowels(word.lower())] = word
        
        res = []
        for query in queries:
            lower = query.lower()
            no_vowels = remove_vowels(lower)
            if query in words:
                res.append(query)
            elif lower in words_lower:
                res.append(words_lower[lower])
            elif no_vowels in words_vowels_removed:
                res.append(words_vowels_removed[no_vowels])
            else:
                res.append("")
        
        return res
