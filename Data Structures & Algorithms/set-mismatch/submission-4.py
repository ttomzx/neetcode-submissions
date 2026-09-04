class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dup, mis = None, None

        freq = Counter(nums)

        for x, y in freq.items():
            if y == 2:
                dup = x
                break
                
        for i in range(1, len(nums)+1):
            if i not in nums:
                mis = i

        return [dup, mis]