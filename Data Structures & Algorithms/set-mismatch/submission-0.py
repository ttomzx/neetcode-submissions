class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)

        dup = None
        for i, num in freq.items():
            if num == 2:
                dup = i
        nums = set(nums)
        miss = None
        for i in range(len(nums)+2):
            if i not in nums:
                miss = i

        return [dup, miss]