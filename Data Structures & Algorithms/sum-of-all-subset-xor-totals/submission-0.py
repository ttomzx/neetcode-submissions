class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        subsets = [[]]
        suum = 0

        for num in nums:
            new_subset = [[num] + curr for curr in subsets]
            subsets.extend(new_subset)

        for l in subsets:
            xor = 0

            for e in l:
                xor ^= e

            suum += xor

        return suum
        