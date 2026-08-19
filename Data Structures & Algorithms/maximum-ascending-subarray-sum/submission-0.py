class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        best_sum = nums[0]
        new_sum = nums[0]

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                new_sum += nums[i]
            else:
                new_sum = nums[i]
            
            best_sum = max(best_sum, new_sum)

        return best_sum
                