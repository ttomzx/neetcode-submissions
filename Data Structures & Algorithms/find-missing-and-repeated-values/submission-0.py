class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)

        freq = Counter(num for rows in grid for num in rows)

        repeated = next(num for num in freq if freq[num] == 2)
        missing = next(num for num in range(1, n*n+1) if freq[num] == 0)

        return [repeated, missing]
