class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        need = {}
        for ch in t:
            need[ch] = need.get(ch, 0) + 1

        have = {}
        required = len(need)
        formed = 0
        min_len = len(s) + 1
        min_start = 0

        l, r = 0, 0
        while r < len(s):
            ch = s[r]
            have[ch] = have.get(ch, 0) + 1

            if need.get(ch, 0) > 0 and have[ch] == need[ch]:
                formed += 1

            while formed == required:
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    min_start = l

                have[s[l]] -= 1
                if have[s[l]] < need.get(s[l], 0):
                    formed -= 1
                l += 1

            r += 1

        return s[min_start:min_start + min_len] if min_len != len(s) + 1 else ""

