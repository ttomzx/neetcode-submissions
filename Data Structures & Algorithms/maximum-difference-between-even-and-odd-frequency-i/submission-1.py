class Solution:
    def maxDifference(self, s: str) -> int:
        freq = Counter(s)

        a1 = 0
        a2 = 9999
        for x in freq.values():
            if x % 2 != 0:
                a1 = max(x, a1)
            else:
                a2 = min(x, a2)

        return a1-a2