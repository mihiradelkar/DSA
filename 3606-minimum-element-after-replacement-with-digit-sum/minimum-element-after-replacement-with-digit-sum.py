class Solution:
    def minElement(self, nums: List[int]) -> int:
        min_d = 36 # float("inf") # or 36 is the max 10^4 10000 max will be 9999 = 36
        for num in nums:
            s = 0
            # for d in str(num):
            #     s+=int(d)
            while num:
                num, d = divmod(num, 10)
                s+=d
            min_d = min(min_d,s)
        return min_d