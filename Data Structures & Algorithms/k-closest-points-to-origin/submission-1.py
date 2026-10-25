class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        nums = []

        for x, y in points:
            dis = x**2 + y**2
            heapq.heappush(nums, (dis, [x, y]))

        res = []

        for _ in range(k):
            res.append(heapq.heappop(nums)[1])

        return res