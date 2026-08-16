class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)

        dup = None
        for i, num in freq.items():
            if num == 2:
                dup = i
        nums = set(nums)
        n = len(nums) + 1

        miss = abs(n*(n+1) // 2 - sum(nums))

        return [dup, miss]