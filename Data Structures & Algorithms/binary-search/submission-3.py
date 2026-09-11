class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def recursive_binary_search(i, j, target):
            print(i, j)
            if i > j:
                return -1
            if i == j:
                if nums[(i + j) // 2] == target:
                    return (i + j) // 2
                else:
                    return -1
            if target < nums[(i + j) // 2]:
                return recursive_binary_search(i, (i + j) // 2 - 1, target)
            elif target > nums[(i + j) // 2]:
                return recursive_binary_search((i + j) // 2 + 1, j, target)
            else:
                # target == nums[(i + j) // 2]
                return (i + j) // 2

        return recursive_binary_search(0, len(nums) - 1, target)