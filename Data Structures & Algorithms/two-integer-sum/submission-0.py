class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {nums[0]: 0}
        for i, num in enumerate(nums[1:], start = 1):
            if (target - num) in seen:
                return [seen[target - num], i]
            seen[num] = i
