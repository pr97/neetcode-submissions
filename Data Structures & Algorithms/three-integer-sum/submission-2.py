class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 3Sum as a 2Sum extension
        target = 0
        found_triplets = set()
        found_triplet_vals = set()
        for i in range(len(nums)):
            seen = {}
            two_sum_target = target - nums[i]
            for j in range(len(nums)):
                if i == j:
                    continue
                if two_sum_target - nums[j] in seen:
                    k = seen[two_sum_target - nums[j]]
                    if tuple(sorted((i, j, k))) in found_triplets or tuple(sorted((nums[i], nums[j], nums[k]))) in found_triplet_vals:
                        continue
                    else:
                        found_triplets.add(tuple(sorted((i, j, k))))
                        found_triplet_vals.add(tuple(sorted((nums[i], nums[j], nums[k]))))
                else:
                    seen[nums[j]] = j

        return list(set([tuple(map(lambda x: nums[x], index_triplet)) for index_triplet in found_triplets]))
        