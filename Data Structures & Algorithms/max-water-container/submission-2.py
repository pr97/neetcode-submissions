class Solution:
    def getArea(self, heights: List[int], i, j):
        return (heights[i] if heights[i] < heights[j] else heights[j]) * (j - i)
    
    def maxArea(self, heights: List[int]) -> int:
        # O(n^2) - Brute (Expect to go into TLE)
        # max_area = -1
        # for i in range(len(heights)):
        #     for j in range(i, len(heights)):
        #         curr_area = (j - i) * min(heights[i], heights[j])
        #         if curr_area > max_area:
        #             max_area = curr_area
        # return max_area

        # O(n) - Two Pointers
        i = 0
        j = len(heights) - 1
        max_area = self.getArea(heights, i, j)
        while i < j:
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
            
            curr_area = self.getArea(heights, i, j)
            max_area = max(max_area, curr_area)

        return max_area





        