class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = [x for x in range(1, len(nums)+1) if x not in nums]
        return res