class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = Counter(arr)
        maxLucky = -1

        for x, y in freq.items():
            if x == y:
                maxLucky = max(maxLucky, x)

        return maxLucky