class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        best = nums[0]
        newsum = nums[0]

        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                newsum = 0
            newsum += nums[i]
            best = max(best, newsum)

        return best
                