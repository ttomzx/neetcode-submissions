class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        res = []

        for x, y in cnt.items():
            if y > len(nums) // 3:
                res.append(x)

        return res 
