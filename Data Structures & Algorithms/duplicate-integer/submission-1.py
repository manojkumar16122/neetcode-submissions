class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # set1 = set(nums)
        # if len(set1) != len(nums):
        #     return True
        # else:
        #     return False

        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False