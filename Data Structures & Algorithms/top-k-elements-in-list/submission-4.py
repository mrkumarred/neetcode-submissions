class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        import heapq
        c = Counter(nums)
        return heapq.nlargest(k, c, key=c.get)