class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int("".join(map(str, digits))) + 1

        res = []
        for _ in str(num):
            res.append(_)

        return res

        