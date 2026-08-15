class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        pairs = {}
        for i in range(len(names)):
            pairs[heights[i]] = names[i]

        heights = sorted(heights, reverse=True)
        res = []
        for height in heights:
            res.append(pairs[height])

        return res