from itertools import zip_longest

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return all(x == y for x,y in zip_longest(sorted(s), sorted(t)))