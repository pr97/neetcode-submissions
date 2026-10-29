class Solution:
    def find_water_between(self, l: int, r: int, height: List[int]):
        smaller_height = min(height[l], height[r])
        water = 0
        for k in range(l + 1, r):
            water += (smaller_height - height[k])

        return water


    def trap(self, height: List[int]) -> int:
        # # O(nlogn)
        # total_water = 0
        # if len(height) <= 2:
        #     return 0
        # height_with_index = sorted(
        #     [(h, i) for i, h in enumerate(height)],
        #     reverse=True,
        # )
        # seen = False * len(height)
        
        # l = min(height_with_index[0][1], height_with_index[1][1])
        # r = max(height_with_index[0][1], height_with_index[1][1])
        # total_water += self.find_water_between(l, r, height)
        
        # for i in range(2, len(height)):
        #     if height_with_index[i][1] > l and height_with_index[i][1] < r:
        #         continue
        #     elif height_with_index[i][1] > r:
        #         total_water += self.find_water_between(r, height_with_index[i][1], height)
        #         r = height_with_index[i][1]
        #     else:
        #         # i < l
        #         total_water += self.find_water_between(height_with_index[i][1], l, height)
        #         l = height_with_index[i][1]

        # return total_water

        # O(n) - PrefixLeftMax SuffixRightMax
        prefix_left_max = [-1] * len(height)
        suffix_right_max = [-1] * len(height)
        lmax = rmax = -1
        for i in range(len(height)):
            if height[i] > lmax:
                lmax = height[i]
            prefix_left_max[i] = lmax
            
            if height[len(height) - 1 - i] > rmax:
                rmax = height[len(height) - 1 - i]
            suffix_right_max[len(height) - 1 - i] = rmax

        # print("\t".join(map(str, height)))
        # print("\t".join(map(str, prefix_left_max)))
        # print("\t".join(map(str, suffix_right_max)))
        
        total_water = 0
        for i in range(len(height)):
            total_water += (min(prefix_left_max[i], suffix_right_max[i]) - height[i])

        return total_water