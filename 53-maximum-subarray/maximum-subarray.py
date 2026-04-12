class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        # dp   = [-2, 1, -2, 4,  3, 5, 6, -1, 4]
        max_sum = nums[0]
        cur_sum = 0
        for num in nums:
            cur_sum = max(num,num+cur_sum)
            max_sum = max(max_sum,cur_sum)
        return max_sum