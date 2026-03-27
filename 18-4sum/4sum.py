class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # [-2, -1, 0, 0, 1, 2]
        #   i 
        #       j 
        #          l         h
        #  0 - -1  = 1
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n-3):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,n-2):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                lo = j+1
                hi = n-1
                while lo < hi:
                    total = nums[i]+nums[j]+nums[lo]+nums[hi]
                    if total == target:
                        res.append((nums[i],nums[j],nums[lo],nums[hi]))
                        while lo<hi and nums[lo] == nums[lo+1]:
                            lo+=1
                        while lo<hi and nums[hi] == nums[hi-1]:
                            hi-=1
                        lo+=1
                        hi-=1
                    elif total < target:
                        lo+=1
                    else:
                        hi-=1
        return res