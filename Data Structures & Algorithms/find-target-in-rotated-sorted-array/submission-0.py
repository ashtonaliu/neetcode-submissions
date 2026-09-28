class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        # Step 1: Find the rotation point (smallest element)
        low = 0
        high = n - 1

        while low < high:
            mid = low + (high - low) // 2

            if nums[mid] > nums[high]:
                # Rotation point must be to the right of mid
                low = mid + 1
            else:
                # Rotation point is at mid or to the left
                high = mid

        pivot = low

        # Step 2: Figure out which sorted half target belongs to
        if nums[pivot] <= target <= nums[n - 1]:
            low = pivot
            high = n - 1
        else:
            low = 0
            high = pivot - 1

        # Step 3: Normal binary search
        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                return mid

        return -1