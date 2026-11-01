class Solution:
    # def findMin(self, nums: List[int]) -> int:
    #     l = 0
    #     r = len(nums) - 1
    #     if nums[l] < nums[r] or len(nums) == 1:
    #         return l
    #     while r >= l:
    #         mid = (l + r) // 2
    #         if mid - 1 >= 0 and nums[mid] < nums[mid - 1]:
    #             return mid
    #         elif mid + 1 < len(nums) and nums[mid] > nums[mid + 1]:
    #             return mid + 1
    #         if nums[l] < nums[mid] and nums[r] < nums[mid]:
    #             l = mid + 1
    #         elif nums[l] > nums[mid] and nums[r] > nums[mid]:
    #             r = mid - 1
    # def binary_search(self, nums: List[int], target: int, l: int, r: int) -> int:
    #     while l <= r:
    #         mid = (l + r) // 2
    #         if nums[mid] == target:
    #             return mid
    #         elif nums[mid] < target:
    #             l = mid + 1
    #         else:
    #             r = mid - 1
    #     return -1
    # def search(self, nums: List[int], target: int) -> int:
    #     pivot = self.findMin(nums)
    #     left_search = self.binary_search(nums, target, 0, pivot - 1)
    #     right_search = self.binary_search(nums, target, pivot, len(nums) - 1)
    #     return max(left_search, right_search)

    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid

            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1

            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1

        