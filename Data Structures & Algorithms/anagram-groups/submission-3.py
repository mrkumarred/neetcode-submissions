class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
            from collections import defaultdict
            seen = defaultdict(list)
            for elem in strs:
                count = [0] * 26
                for ch in elem:
                    count[ord(ch) - ord('a')] += 1
                seen[tuple(count)].append(elem)
            
            return list(seen.values())