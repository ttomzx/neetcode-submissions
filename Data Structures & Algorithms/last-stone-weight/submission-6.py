class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]

        heapq.heapify(stones)

        while len(stones) > 1:
            w1 = -heapq.heappop(stones)
            w2 = -heapq.heappop(stones)

            if w1 != w2:
                heapq.heappush(stones, -(w1 - w2))

        return -stones[0] if stones else 0