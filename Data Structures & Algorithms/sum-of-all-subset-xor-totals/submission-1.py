class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        res, sol = [], []

        def bt(i):
            if i == n:
                x = 0
                for num in sol:
                   x ^= num 
                res.append(x)
                return

            bt(i+1)

            sol.append(nums[i])
            bt(i+1)
            sol.pop()

        bt(0)
        return sum(res)
        