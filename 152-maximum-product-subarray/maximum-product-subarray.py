class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #    [   2,  3, -2,  4, -1]
        #   2    2   3  -2   4  -1
        #   6    3  -2   4  -1  
        # -12   -2   4  -1
        # -48    4  -1
        #  48   -1
        #  
        res = float("-inf")
        cur_max = cur_min = 1
        for num in nums:
            cur_max, cur_min = max(cur_max*num, cur_min*num, num), min(cur_max*num, cur_min*num, num)
            # print(cur_max, cur_min)
            res = max(res, cur_max)
        return res

        