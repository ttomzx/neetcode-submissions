class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set([n1 for n1 in nums1 if n1 in nums2]))