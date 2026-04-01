class Solution:
    def rob(self, nums: List[int]) -> int:
        # [2   7   9   5   1  10]
        #  2   7  11   
        n = len(nums)
        prev = curr = 0
        for i in range(n):
            curr,prev = max(curr,prev+nums[i]), curr
        return curr