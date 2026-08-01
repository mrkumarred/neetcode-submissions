class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 1 :
           return 0

        sm = {}
        l=0
        res = 0
        for r in range (len (s)):
            if s[r] in sm:
                l = max(sm[s[r]] +1, l)
            sm[s[r]] = r
            res = max(res, r-l +1)
        return res
      