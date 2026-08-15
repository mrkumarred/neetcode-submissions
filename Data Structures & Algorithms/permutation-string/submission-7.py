class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = [0] * 26
        s2_count = [0] * 26
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1

        matches = sum(1 for i in range(26) if s1_count[i] == s2_count[i])
        if matches == 26:
            return True

        for i in range(len(s1), len(s2)):
            enter = ord(s2[i]) - ord('a')
            leave = ord(s2[i - len(s1)]) - ord('a')

            if s2_count[enter] == s1_count[enter]:
                matches -= 1
            s2_count[enter] += 1
            if s2_count[enter] == s1_count[enter]:
                matches += 1

            if s2_count[leave] == s1_count[leave]:
                matches -= 1
            s2_count[leave] -= 1
            if s2_count[leave] == s1_count[leave]:
                matches += 1

            if matches == 26:
                return True

        return False