class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        subset = []

        def bt(open, close):
            if len(subset) == n*2:
                res.append("".join(subset.copy()))
                return

            if open < n:
                subset.append("(")
                bt(open+1, close)
                subset.pop()

            if close < open:
                subset.append(")")
                bt(open, close+1)
                subset.pop()

        bt(0, 0)
        return res