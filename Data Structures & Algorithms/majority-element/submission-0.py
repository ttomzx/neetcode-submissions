class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        count = sorted(count.items(), key=lambda x:x[1], reverse=True)
        
        return count[0][0]