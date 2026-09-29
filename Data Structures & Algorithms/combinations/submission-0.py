class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(1, n+1)]
        print(nums)
        res, sol = [], []

        def bt(i):
            if len(sol) == k:
                res.append(sol[:])
                return

            if i == n:
                return

            bt(i+1)

            sol.append(nums[i])
            bt(i+1)
            sol.pop()

        bt(0)
        return res
        