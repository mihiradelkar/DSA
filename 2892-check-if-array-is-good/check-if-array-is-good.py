class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums.sort()
        n = len(nums)
        if n < 2:
            return False
        for i in range(n-1):
            if nums[i] != i+1:
                return False
        return True if nums[-1]==nums[-2] and nums[-1]==n-1 else False