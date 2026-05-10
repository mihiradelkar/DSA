class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        # n = len(nums) 
        # i = 0
        # j = 1
        # jump = 0
        # while j<n:
        #     if abs(nums[j] - nums[i]) <= target:
        #         jump+=1
        #         i=j
        #     j+=1
        # return -1 if i!=n-1 else jump
        
        n = len(nums) 
        jumps=[-1]*n
        jumps[0]=0
        for j in range(1,n):
            for i in range(j):
                if abs(nums[j] - nums[i]) <= target and jumps[i] != -1:
                    jumps[j] = max(jumps[j],jumps[i]+1)
        return jumps[n-1]



        