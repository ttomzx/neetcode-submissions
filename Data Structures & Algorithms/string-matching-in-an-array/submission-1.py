class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = []
        
        for word in words:
            for i in range(len(words)):
                if word != words[i] and word in words[i]:
                    ans.append(word)

        return list(set(ans))