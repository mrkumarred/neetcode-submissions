class Solution:
    def isValid(self, s: str) -> bool:
        # Edge case: odd length string can never be valid
        if len(s) % 2 != 0:
            return False

        # Stack to track opening brackets (LIFO structure)
        stack = []

        # Map closing brackets to their matching opening brackets
        bracket_map = {')': '(', ']': '[', '}': '{'}

        for char in s:
            if char in bracket_map.values():
                # Opening bracket: push to stack
                stack.append(char)
            elif char in bracket_map.keys():
                # Closing bracket: must match the most recent opening bracket
                if not stack or stack[-1] != bracket_map[char]:
                    return False
                stack.pop()

        # Valid only if no opening brackets remain unmatched
        return len(stack) == 0