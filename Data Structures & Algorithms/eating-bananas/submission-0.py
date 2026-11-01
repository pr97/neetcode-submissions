import math
class Solution:
    def find_time_for_k(self, piles, k):
        # O(n)
        return sum([math.ceil(pile / max(k, 1)) for pile in piles])
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles) # O(n)
        while r - l >= 0:
            mid = (l + r) // 2
            time = self.find_time_for_k(piles, mid)
            found_rate = mid
            if time <= h:
                if self.find_time_for_k(piles, mid - 1) > h:
                    return mid
                r = mid - 1
            else:
                l = mid + 1
        return mid

        