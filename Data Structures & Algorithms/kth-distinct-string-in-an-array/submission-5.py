class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        
        
        freq = Counter(arr)

        dist = []
        for x, y in freq.items():
            if y == 1:
                dist.append(x)

        if len(dist) < k:
            return ""
        
        return dist[k-1]