class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "<E>"
        return '#*#'.join(strs)
    def decode(self, s: str) -> List[str]:
        if s == "<E>":
            return []
        return s.split('#*#')
