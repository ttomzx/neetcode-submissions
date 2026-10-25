class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)

        i = len(nums)
        while i > k:
            heapq.heappop(nums)
            i -= 1

        return heapq.heappop(nums)
        