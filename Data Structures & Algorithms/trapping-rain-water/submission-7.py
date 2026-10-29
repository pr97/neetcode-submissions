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
        # prefix_left_max = [-1] * len(height)
        # suffix_right_max = [-1] * len(height)
        # lmax = rmax = -1
        # for i in range(len(height)):
        #     if height[i] > lmax:
        #         lmax = height[i]
        #     prefix_left_max[i] = lmax
            
        #     if height[len(height) - 1 - i] > rmax:
        #         rmax = height[len(height) - 1 - i]
        #     suffix_right_max[len(height) - 1 - i] = rmax

        # # print("\t".join(map(str, height)))
        # # print("\t".join(map(str, prefix_left_max)))
        # # print("\t".join(map(str, suffix_right_max)))
        
        # total_water = 0
        # for i in range(len(height)):
        #     total_water += (min(prefix_left_max[i], suffix_right_max[i]) - height[i])

        # return total_water

        # O(n) - Two Pointer
        # total_water = 0
        # lPtr = 0
        # rPtr = len(height) - 1
        # lMax = rMax = -1

        # while lPtr < rPtr:
        #     lMax = max(lMax, height[lPtr])
        #     rMax = max(rMax, height[rPtr])
        #     # print(f"lPtr={lPtr} rPtr={rPtr}")
        #     # print(f"lMax={lMax} rMax={rMax}")
        #     # print(f"height[lPtr]={height[lPtr]} height[rPtr]={height[rPtr]}")
        #     if height[lPtr] < height[rPtr]:
        #         calPtr = lPtr
        #         lPtr += 1
        #     else:
        #         calPtr = rPtr
        #         rPtr -= 1
        #     # print(f"lPtr={lPtr} rPtr={rPtr} calPtr={calPtr}")
        #     total_water += min(lMax, rMax) - height[calPtr]
        #     # print(f"total_water={total_water}")
        #     # calPtr = lPtr if height[lPtr] < height[rPtr] else rMax
        #     # print("+++++++++++++++++++")

        # return total_water

        # O(n) - Stack Approach - Level by level (horizontal filling)
        total_water = 0
        stack = [None]
        for i in range(len(height)):
            if stack[-1] is None:
                stack.append(i)
            else:
                while stack[-1] is not None and height[i] > height[stack[-1]]:
                    b = stack.pop()
                    l = stack[-1]
                    if l is None:
                        pass
                    else:
                        width = i - l - 1
                        total_water += ((min(height[i], height[l]) - height[b]) * width)
                stack.append(i)
        return total_water

