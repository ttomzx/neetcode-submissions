class Solution:
    def minOperations(self, s: str) -> int:
        count0 = 0
        for i, ch in enumerate(s):
            expected = '0' if i % 2 == 0 else '1'
            if ch != expected:
                count0 += 1

        return min(count0, len(s) - count0)