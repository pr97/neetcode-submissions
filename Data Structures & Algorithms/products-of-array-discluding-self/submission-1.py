class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # # Base O(n) solution (using division)
        # prod = 1 # this is suppose to contain the product of all non-zero numbers
        # num_zeros = 0
        # for x in nums:
        #     if x != 0:
        #         prod *= x
        #     else:
        #         num_zeros += 1
        
        # res = []
        # for x in nums:
        #     if num_zeros > 1:
        #         res.append(0)
        #     elif num_zeros == 1:
        #         if x == 0:
        #             res.append(prod)
        #         else:
        #             res.append(0)
        #     else:
        #         res.append(prod // x)

        # return res

        # O(n) without division
        left = []
        right = []
        res = [1] * len(nums)
        
        left_prod = 1
        for i in range(len(nums)):
            left_prod *= nums[i]
            if i + 1 < len(nums):
                res[i + 1] *= left_prod
            
        right_prod = 1
        for i in range(-1, -(len(nums) + 1), -1):
            right_prod *= nums[i]
            if i - 1 >= -len(nums):
                res[i - 1] *= right_prod

        return res

            
