from typing import List, Any, Callable

class PriorityQueue:
    def __init__(self, comparator: Callable = lambda a, b: a < b, type: str = "min"):
        self.type: str = type
        self.comparator: Callable = comparator
        self.heap: List[Any] = []

    def __len__(self):
        return len(self.heap)

    def left_child(self, index: int):
        return 2 * index + 1

    def right_child(self, index: int):
        return 2 * index + 2

    def parent(self, index: int):
        return (index - 1) // 2

    def is_valid_index(self, index: int):
        return index >= 0 and index < len(self)

    def swap(self, i: int, j: int):
        temp_ = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = temp_

    def bubble_up(self, index: int):
        if index == 0:
            return
        while (
            self.is_valid_index(self.parent(index))
            and self.comparator(self.heap[index], self.heap[self.parent(index)])
        ):
            self.swap(index, self.parent(index))
            index = self.parent(index)

    def bubble_down(self, index: int):
        # We only need to check left_child because a right child can't exist without a left one
        while self.is_valid_index(self.left_child(index)):
            left = self.left_child(index)
            right = self.right_child(index)

            # Assume left child is the extreme (e.g., smallest in a min-heap)
            extreme_child = left

            # If right child exists AND is more extreme than left child, update our target
            if self.is_valid_index(right) and self.comparator(self.heap[right], self.heap[left]):
                extreme_child = right

            # If the current node is already more extreme than the best child, heap property is met
            if self.comparator(self.heap[index], self.heap[extreme_child]):
                break

            # Otherwise, swap and move down the tree
            self.swap(index, extreme_child)
            index = extreme_child

    def push(self, val: Any):
        self.heap.append(val)
        val_idx = len(self) - 1
        self.bubble_up(val_idx)

    def pop(self):
        if len(self) == 0:
            raise IndexError("pop from empty heap")
        top = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.bubble_down(0)
        return top

    def peek(self):
        if len(self) == 0:
            return -1
        return self.heap[0]

class Solution:
    def find_water_between(self, l: int, r: int, height: List[int]):
        smaller_height = min(height[l], height[r])
        water = 0
        # seen[l] = True
        # seen[r] = True
        for k in range(l + 1, r):
            water += (smaller_height - height[k])
            # seen[k] = True

        return water


    def trap(self, height: List[int]) -> int:
        # heap = PriorityQueue(comparator=lambda a, b: a < b, type="max")
        # for h in height:
        #     heap.push(height)
        total_water = 0
        if len(height) <= 2:
            return 0
        height_with_index = sorted(
            [(h, i) for i, h in enumerate(height)],
            reverse=True,
        )
        seen = False * len(height)
        
        l = min(height_with_index[0][1], height_with_index[1][1])
        r = max(height_with_index[0][1], height_with_index[1][1])
        total_water += self.find_water_between(l, r, height)
        # print("base:", l, r, total_water)
        # print(height_with_index)
        
        for i in range(2, len(height)):
            if height_with_index[i][1] > l and height_with_index[i][1] < r:
                continue
            elif height_with_index[i][1] > r:
                total_water += self.find_water_between(r, height_with_index[i][1], height)
                r = height_with_index[i][1]
                # print("i>r:", l, r, "|",  i, total_water)
            else:
                # i < l
                total_water += self.find_water_between(height_with_index[i][1], l, height)
                l = height_with_index[i][1]
                # print("i<l:", l, r, "|",  i, total_water)

        return total_water








        