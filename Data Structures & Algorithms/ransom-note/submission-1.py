class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magCount = Counter(magazine)
        ranCount = Counter(ransomNote)

        for ch, val in ranCount.items():
            if magCount[ch] < val:
                return False
        
        return True