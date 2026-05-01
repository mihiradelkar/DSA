class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        # n = len(nums)
        # res = 0
        # if n == 0:
        #     return 0
        # Brute Force:
        # for i in range(n):
        #     fsum = 0
        #     for j in range(n):
        #         k = (i + j) % n
        #         fsum+= j * nums[k]
        #         # print(i,j,fsum)
        #     res = max(res,fsum)
        
        # Optimal: deriving a recurrence
        n = len(nums)
        if n == 0:
            return 0
        total = sum(nums)
        f = sum(i*nums[i] for i in range(n))    # F0
        res = f
        for k in range(1,n):
            f = f + total - n * nums[n-k]       # F[k] = F[k-1] + total - n * nums[n-k]
            res = max(res,f)                    #     prev + all ele once - reduce the nums[n-k] by n times to og
        return res

    # Setup: what does one rotation step actually do?
        # Each rotation shifts the array so the last element wraps to the front. Going from rotation k−1 to
        # rotation k, every element's index increases by 1 — except one element, which drops from index n−1 all
        # the way back to index 0.
    # Tracking the weight change for every element:
        # Every element's coefficient goes from i to i+1 — a gain of 1. Summed across all elements, 
        # that's +totalSum.
        # But one element — nums[n-k] — is the one wrapping around. Its coefficient doesn't increase by 1; it 
        # falls from n−1 all the way to 0. So instead of gaining 1, it drops by n−1. 
        # The net correction is −(n−1) − 1 = −n, giving −n * nums[n-k].
