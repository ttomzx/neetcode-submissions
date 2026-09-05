class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []

        for i in range(n+1):
            res.append(sum(1 for x in str(bin(i)) if x == "1"))

        return res