class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        res, sol = [], []

        def bt(i, total):
            if total == target:
                res.append(sol[:])
                return

            if i == n or total > target:
                return

            bt(i+1, total)

            sol.append(nums[i])
            bt(i, total + nums[i])
            sol.pop()


        bt(0, 0)
        return res
        