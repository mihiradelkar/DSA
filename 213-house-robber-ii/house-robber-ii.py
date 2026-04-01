class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        def rob(start,end):            
            prev = curr = 0
            for i in range(start,end):
                prev, curr = curr, max(curr,prev+nums[i])
            return curr
        return max(nums[0],rob(0,n-1),rob(1,n))
        