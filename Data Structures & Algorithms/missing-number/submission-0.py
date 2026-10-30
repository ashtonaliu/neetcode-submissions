class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        def orderedSum(n):
            total = 0
            for i in range(1, n + 1):
                total += i
            return total
        t = orderedSum(len(nums))
        s = sum(nums)
        if s == t:
            return 0
        return t - s
        