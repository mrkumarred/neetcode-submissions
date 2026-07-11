class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        seen = defaultdict(list)
        for elem in strs:
            sorted_elem = "".join(sorted(elem))
            seen[sorted_elem].append(elem)

        return list(seen.values())
