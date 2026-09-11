class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def recursive_binary_search(i, j, target):
            print(i, j)
            mid = (i + j) // 2
            if i > j:
                return -1
            if target < nums[mid]:
                return recursive_binary_search(i, mid - 1, target)
            elif target > nums[mid]:
                return recursive_binary_search(mid + 1, j, target)
            else:
                return mid

        return recursive_binary_search(0, len(nums) - 1, target)