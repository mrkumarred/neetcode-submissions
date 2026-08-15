class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        # Arrays to store the frequency of characters (a-z)
        s1_count = [0] * 26
        s2_count = [0] * 26

        # Initialize the frequency counts for s1 and the first window of s2
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1

        if s1_count == s2_count:
            return True

        # Slide the window over the rest of s2
        for i in range(len(s1), len(s2)):
            # Add the new character entering the window
            s2_count[ord(s2[i]) - ord('a')] += 1
            # Remove the character leaving the window
            s2_count[ord(s2[i - len(s1)]) - ord('a')] -= 1
            # Check if the current window is a permutation
            if s1_count == s2_count:
                return True

        return False