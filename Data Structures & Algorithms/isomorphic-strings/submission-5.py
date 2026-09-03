class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        seenS = {}
        seenT = {}

        for a, b in zip(s, t):
            if a in seenS and seenS[a] != b:
                return False
            if b in seenT and seenT[b] != a:
                return False

            seenS[a] = b
            seenT[b] = a

        return True