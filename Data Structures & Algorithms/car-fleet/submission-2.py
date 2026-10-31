class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # O(nlogn) - Sorting by position and then iterating from the back, keeping track.
        pst = [
            (
                position[i],
                speed[i],
                ((target - position[i]) / speed[i]),
            ) for i in range(len(speed))
        ]
        pst = sorted(pst)
        fleet_ctr = 0
        curr_lim = -1
        for i in range(len(pst) - 1, -1, -1):
            # print(i)
            # print(pst)
            # print(curr_lim)
            # print(f"pre: {fleet_ctr}")
            if i == len(pst) - 1:
                fleet_ctr += 1
                curr_lim = pst[i][2]
            else:
                if pst[i][2] <= curr_lim:
                    continue
                else:
                    fleet_ctr += 1
                    curr_lim = pst[i][2]
            # print(f"post: {fleet_ctr}")
            # print("++++++++++")
        return fleet_ctr

    # O(1) space
    # def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
    #     n = len(position)
    #     if n <= 1:
    #         return n

    #     # In-place Heapsort to achieve O(n log n) time and O(1) auxiliary space
    #     def heapify(length: int, i: int):
    #         largest = i
    #         left = 2 * i + 1
    #         right = 2 * i + 2

    #         if left < length and position[left] > position[largest]:
    #             largest = left
    #         if right < length and position[right] > position[largest]:
    #             largest = right

    #         if largest != i:
    #             # Synchronized in-place swap
    #             position[i], position[largest] = position[largest], position[i]
    #             speed[i], speed[largest] = speed[largest], speed[i]
    #             heapify(length, largest)

    #     # Build max heap
    #     for i in range(n // 2 - 1, -1, -1):
    #         heapify(n, i)

    #     # Extract elements one by one
    #     for i in range(n - 1, 0, -1):
    #         position[0], position[i] = position[i], position[0]
    #         speed[0], speed[i] = speed[i], speed[0]
    #         heapify(i, 0)

    #     # Linear scan from back to front, computing time on the fly
    #     fleet_ctr = 0
    #     curr_lim = -1.0
    #     for i in range(n - 1, -1, -1):
    #         time = (target - position[i]) / speed[i]
    #         if time > curr_lim:
    #             fleet_ctr += 1
    #             curr_lim = time

    #     return fleet_ctr