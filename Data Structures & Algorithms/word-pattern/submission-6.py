class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if len(pattern) != len(s.split()):
            return False
        s = s.split()
        wordtochar = {}
        chartoword = {}

        for p, s in zip(pattern, s):
            if p in chartoword and chartoword[p] != s:
                return False

            if s in wordtochar and wordtochar[s] != p:
                return False

            wordtochar[s] = p
            chartoword[p] = s

        return True