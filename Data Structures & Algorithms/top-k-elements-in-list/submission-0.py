from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # O(nlogn)
        c = Counter(nums)
        counts = tuple([(c.get(x), x) for x in c])
        counts_sorted = sorted(counts, reverse=True)

        return [x[1] for x in counts_sorted[:k]]

        