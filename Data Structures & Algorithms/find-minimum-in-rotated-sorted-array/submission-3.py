class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        if nums[l] < nums[r] or len(nums) == 1:
            return nums[l]
        while r >= l:
            mid = (l + r) // 2
            if mid - 1 >= 0 and nums[mid] < nums[mid - 1]:
                return nums[mid]
            elif mid + 1 < len(nums) and nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if nums[l] < nums[mid] and nums[r] < nums[mid]:
                l = mid + 1
            elif nums[l] > nums[mid] and nums[r] > nums[mid]:
                r = mid - 1
            

        