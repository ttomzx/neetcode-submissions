class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ind = {}
        size = []

        for c in s:
            ind[c] = s.rfind(c)

        start = 0
        end = 0

        for i, c in enumerate(s):
            end = max(end, ind[c])

            if i == end:
                size.append(end - start + 1)
                start = i + 1

        return size