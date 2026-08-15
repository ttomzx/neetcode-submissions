class Solution:
    def maxDifference(self, s: str) -> int:
        freq = Counter(s)

        a1, a2 = 0, 99999
        for x in freq.values():
            if x % 2 != 0:
                a1 = max(a1, x)

            else:
                a2 = min(a2, x)

        return a1 - a2