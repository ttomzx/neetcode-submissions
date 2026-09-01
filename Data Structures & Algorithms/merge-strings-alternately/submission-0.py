class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""

        i = 0
        for c1, c2 in zip(word1, word2):
            res += c1 + c2
            i += 1

        return res + word1[i:] + word2[i:]