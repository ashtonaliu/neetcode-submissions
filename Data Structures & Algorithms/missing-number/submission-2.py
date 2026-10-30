class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums) + 1
        t = n*(n - 1) // 2
        s = sum(nums)
        return t - s
        