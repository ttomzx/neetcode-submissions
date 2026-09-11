class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = set()
        cnt = Counter(nums)

        for x, y in cnt.items():
            if y > len(nums) // 3:
                res.add(x)

        return list(res)
