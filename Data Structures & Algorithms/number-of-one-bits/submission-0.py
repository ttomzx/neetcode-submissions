class Solution:
    def hammingWeight(self, n: int) -> int:
       return sum(1 for x in str(bin(n)) if x == "1") 