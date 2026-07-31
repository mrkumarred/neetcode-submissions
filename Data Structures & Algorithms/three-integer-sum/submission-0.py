class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = set()
        nums_len = len(nums)
        for i in range(nums_len):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            right = nums_len - 1
            left = i + 1
            while left < right :
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    results.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif total > 0:
                    right -= 1
                elif total < 0 :
                    left += 1
        return [list(elem) for elem in results]