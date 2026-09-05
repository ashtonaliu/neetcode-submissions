class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for i in range(len(nums)):
            num = target - nums[i]
            if num in indices:
                return [indices[num], i]
            else:
                indices[nums[i]] = i