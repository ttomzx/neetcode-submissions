class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = 0

        freq1 = Counter(chars)
        for word in words:
            freq2 = Counter(word)
            if all(freq2[ch] <= freq1[ch] for ch in freq2):
                count += len(word)
        
        return count