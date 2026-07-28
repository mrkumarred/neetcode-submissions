class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums_set = set(nums)
        longest = 1
        for num in nums_set:
            count = 1
            if num - 1 in nums_set:
                # skip the intermediate sequence.
                continue
            while num + count in nums_set:
                count += 1
            longest = max(longest, count)
        return longest