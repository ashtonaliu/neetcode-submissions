class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        list = []
        for i in range(len(nums)):
            if nums[i] in list:
                return True
            list.append(nums[i])
        return False
