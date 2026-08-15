class Solution:
    def isPalindrome(self, x: int) -> bool:
        return False if x < 0 or x != int(str(x)[::-1]) else True