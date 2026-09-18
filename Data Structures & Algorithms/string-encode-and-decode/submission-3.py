class Solution:

    def encode(self, strs: List[str]) -> str:
        num_strs = len(strs)
        str_lens = [len(s) for s in strs]
        length_encode = ".".join([str(num_strs)] + [str(l) for l in str_lens])
        return length_encode + "." + "".join(strs)

    def decode(self, s: str) -> List[str]:
        num_strs_delim_index = s.find(".")
        if num_strs_delim_index == -1:
            return []
        
        num_strs = int(s[:num_strs_delim_index])
        if num_strs == 0:
            return []
        
        delim_indices = []
        found_count = 0
        for idx in range(num_strs_delim_index + 1, len(s)):
            if s[idx] == ".":
                delim_indices.append(idx)
                found_count += 1
            if found_count == num_strs:
                break

        str_lens = []
        prev = num_strs_delim_index
        for x in delim_indices:
            str_lens.append(int(s[(prev + 1):x]))
            prev = x

        actual_concat = s[delim_indices[-1] + 1:]

        res = []
        prev = 0
        for str_len in str_lens:
            res.append(actual_concat[prev : (prev + str_len)])
            prev += str_len

        return res

        

