class Solution:
    def swap_in_nums(self, nums: List[int], idx: int, p: int):
            t = nums[idx]
            nums[idx] = nums[p]
            nums[p] = t
    
    def partition(self, arr, low, high, comp_func):
        p = high
        j = low - 1
        
        for i in range(low, high):
            if comp_func(arr[i], arr[p]):
                j += 1
                self.swap_in_nums(arr, i, j)
        
        j += 1
        self.swap_in_nums(arr, j, p)
        p = j
        
        return p
    
    def quickSort(self, arr, low, high, comp_func):
        # recursive implementation
        # if low < high:
        #     p = self.partition(arr, low, high)
        #     self.quickSort(arr, low, p - 1)
        #     self.quickSort(arr, p + 1, high)
        
        # iterative implementation
        stack = []
        stack.append((low, high))
        while stack:
            low, high = stack.pop()
            if low < high:
                p = self.partition(arr, low, high, comp_func)
                stack.append((low, p - 1))
                stack.append((p + 1, high))

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nlogn
        nums_with_pairs = [(x, idx) for idx, x in enumerate(nums)]
        def comp_func(a, b):
            return a[0] < b[0]
        self.quickSort(nums_with_pairs, 0, len(nums) - 1, comp_func)
        i = 0
        j = len(nums_with_pairs) - 1
        while i < j:
            if nums_with_pairs[i][0] + nums_with_pairs[j][0] < target:
                i += 1
            elif nums_with_pairs[i][0] + nums_with_pairs[j][0] > target:
                j -= 1
            else:
                # nums_with_pairs[i] == nums_with_pairs[j]
                return sorted([nums_with_pairs[i][1], nums_with_pairs[j][1]])

        