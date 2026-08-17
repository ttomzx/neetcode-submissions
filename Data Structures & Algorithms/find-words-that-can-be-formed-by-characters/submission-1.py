class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        s = 0
        count_chars = Counter(chars)

        for word in words:
            count_word = Counter(word)
                
            if count_word <= count_chars:
                s += len(word)

        return s