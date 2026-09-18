class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Base O(n) solution (using division)
        prod = 1 # this is suppose to contain the product of all non-zero numbers
        num_zeros = 0
        for x in nums:
            if x != 0:
                prod *= x
            else:
                num_zeros += 1
        
        res = []
        for x in nums:
            if num_zeros > 1:
                res.append(0)
            elif num_zeros == 1:
                if x == 0:
                    res.append(prod)
                else:
                    res.append(0)
            else:
                res.append(prod // x)

        return res
            
