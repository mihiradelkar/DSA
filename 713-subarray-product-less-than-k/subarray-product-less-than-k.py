class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        l = 0
        total  = 1
        count = 0
        for r in range(len(nums)):
            total *= nums[r]
            while total>=k:
                total //= nums[l]
                l+=1
            count += r-l+1
        return count