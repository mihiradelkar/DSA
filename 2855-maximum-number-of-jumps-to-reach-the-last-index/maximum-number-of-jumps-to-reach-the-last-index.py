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
        for i in range(n):
            if jumps[i] == -1:
                continue
            for j in range(i+1,n):
                if abs(nums[j] - nums[i]) <= target:
                    jumps[j] = max(jumps[j],jumps[i]+1)
        return jumps[n-1]



        