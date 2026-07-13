import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        for i in range(len(nums)):
            result[i] = math.prod(nums[:i] + nums[i+1:])
        return result
