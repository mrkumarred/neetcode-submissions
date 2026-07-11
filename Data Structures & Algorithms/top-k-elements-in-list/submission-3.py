class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        c = Counter(nums)
        bucket = [[] for i in range(len(nums) + 1)]
        for num, freq in c.items():
            bucket[freq].append(num)
        
        res = []
        for i in range(len(bucket) -1 , 0, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res
        return res