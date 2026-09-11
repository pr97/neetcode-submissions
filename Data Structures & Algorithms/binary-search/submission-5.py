class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def recursive_binary_search(i, j, target):
            print(i, j)
            mid = (i + j) // 2
            if i > j:
                return -1
            if i == j:
                if nums[mid] == target:
                    return mid
                else:
                    return -1
            if target <= nums[mid]:
                return recursive_binary_search(i, mid - 0, target)
            elif target > nums[mid]:
                return recursive_binary_search(mid + 1, j, target)
            # else:
            #     # target == nums[mid]
            #     return mid

        return recursive_binary_search(0, len(nums) - 1, target)