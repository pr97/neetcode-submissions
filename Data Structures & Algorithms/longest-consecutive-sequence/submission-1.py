class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not len(nums):
            return 0
        seen = set(nums)
        sequence_starts = set()
        for x in nums:
            if not x - 1 in seen:
                sequence_starts.add(x)
        
        curr_max = 1
        for x in sequence_starts:
            curr_seq_len = 1
            seq_ele = x
            while seq_ele + 1 in seen:
                curr_seq_len += 1
                seq_ele += 1
            if curr_seq_len > curr_max:
                curr_max = curr_seq_len
        
        return curr_max
        