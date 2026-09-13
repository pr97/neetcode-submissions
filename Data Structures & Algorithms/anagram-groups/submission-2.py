import random
import hashlib
from collections import Counter, defaultdict
class QuickSort:
    @staticmethod
    def swap_in_array(arr, i, j):
        t = arr[i]
        arr[i] = arr[j]
        arr[j] = t

    @staticmethod
    def partition(arr, low, high, comp_func):
        # Pick a random pivot and swap it to the end
        pivot_idx = random.randint(low, high)
        QuickSort.swap_in_array(arr, pivot_idx, high)

        j = low - 1
        for i in range(low, high):
            if comp_func(arr[i], arr[high]):
                j += 1
                QuickSort.swap_in_array(arr, i, j)

        j += 1
        QuickSort.swap_in_array(arr, j, high)
        
        return j

    @staticmethod
    def sort(arr, comp_func = lambda a, b: a < b):
        stack = []
        stack.append((0, len(arr) - 1))
        while stack:
            low, high = stack.pop()
            if low < high:
                p = QuickSort.partition(arr, low, high, comp_func)
                stack.append((low, p - 1))
                stack.append((p + 1, high))

class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # O(mnlogn)
        # strs_paired = [(s, sorted(s)) for s in strs]
        # QuickSort.sort(strs_paired, lambda a, b: a[1] < b[1])
        # res = []
        # curr = []
        # for idx, s in enumerate(strs_paired):
        #     if idx == 0:
        #         curr.append(s[0])
        #     else:
        #         if s[1] == strs_paired[idx - 1][1]:
        #             curr.append(s[0])
        #         else:
        #             res.append(curr)
        #             curr = [s[0]]
        
        # res.append(curr)

        # return res

        # O(mn)
        def counter_hash(s):
            """
            O(m)
            """
            c = Counter(s) # O(m)
            sorted_counter_as_string = str(sorted(tuple(dict(c).items())))
            hash_ = hashlib.md5(sorted_counter_as_string.encode("utf-8")).hexdigest()
            return hash_

        counter_hashed_strs = list(map(counter_hash, strs)) # O(mn)

        # O(n)
        anagram_map = defaultdict(list)
        for i in range(len(strs)):
            anagram_map[counter_hashed_strs[i]].append(strs[i])

        res = [v for k, v in anagram_map.items()]

        return res

            



        