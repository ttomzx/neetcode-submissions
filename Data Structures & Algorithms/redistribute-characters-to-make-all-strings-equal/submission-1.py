class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        s = "".join(words)
        cnt = Counter(s)

        for x, y in cnt.items():
            if y % len(words) != 0:
                return False

        return True