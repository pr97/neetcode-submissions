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