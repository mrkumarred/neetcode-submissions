class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        if k >= n: return n
        freq = {i:0 for i in s}
        left  = max_freq = best = 0

        for r in range(len(s)):
            c = s[r]
            freq[c] = freq.get(c, 0) + 1
            if freq[c] > max_freq:
                max_freq = freq[c]
            if (r - left + 1) - max_freq > k:
                freq[s[left]] -= 1
                left += 1
            best = max(best, r - left + 1)
        
        return best