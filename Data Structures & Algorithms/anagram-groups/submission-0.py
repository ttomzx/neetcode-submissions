class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mem = defaultdict(list)

        for s in strs:
            mem[str(sorted(s))].append(s)

        return list(mem.values())           