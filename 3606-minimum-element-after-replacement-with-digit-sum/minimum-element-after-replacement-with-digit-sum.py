class Solution:
    def minElement(self, nums: List[int]) -> int:
        min_d = float("inf")
        for num in nums:
            s = 0
            # for d in str(num):
            #     s+=int(d)
            while num:
                num, d = divmod(num, 10)
                s+=d
            min_d = min(min_d,s)
        return min_d