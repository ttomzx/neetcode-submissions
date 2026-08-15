class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        
        total_prod = 1
        zero_count = nums.count(0)
        
        if zero_count > 1:
            return [0] * len(nums)
            
        for x in nums:
            if x != 0: total_prod *= x
            
        for i in range(len(nums)):
            if zero_count == 1:
                output.append(total_prod if nums[i] == 0 else 0)
            else:
                output.append(total_prod // nums[i])
        
        return output