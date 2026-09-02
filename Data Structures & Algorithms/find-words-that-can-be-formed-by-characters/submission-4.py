class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        cntChar = Counter(chars)
        cnt = 0

        for word in words:
            cntWord = Counter(word)
            
            for x, y in cntWord.items():
                if y > cntChar[x]:
                    break
            else:
                cnt += len(word)

        return cnt