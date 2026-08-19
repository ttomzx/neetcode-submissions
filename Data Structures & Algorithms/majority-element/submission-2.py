class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = Counter(nums)
        for num, count in freq.items():
            if count > len(nums) // 2:
                return num
