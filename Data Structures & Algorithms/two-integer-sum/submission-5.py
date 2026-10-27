class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for x, y in enumerate(nums):
            comp = target - y
            if comp in seen:
                return [seen[comp], x]

            seen[y] = x
        