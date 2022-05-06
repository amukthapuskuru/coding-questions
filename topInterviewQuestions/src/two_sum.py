from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsdict = {}
        for i, c in enumerate(nums):
            complement = target - c
            if complement in numsdict:
                return [numsdict[complement], i]
            numsdict[c] = i

a = Solution()
print(a.twoSum([2, 7, 11, 15], 9))
"""        for i in range(len(nums)):
            for j in range(i + 1, len(nums))
                if nums[i] + nums[j] == target:
                    return i, j """


# Input: nums = [2,7,11,15], target = 9
