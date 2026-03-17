class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # zeros = 0
        # left = 0
        # max_window = 0
        # # [1,1,1,0,0,0,1,1,1,1,0]
        # #            l
        # #                      r
        # for right in range(len(nums)):
        #     if nums[right]==0:
        #         zeros+=1
        #     while zeros>k:
        #         if nums[left]==0:
        #             zeros-=1
        #         left+=1
        #     max_window = max(max_window,right-left+1)
        # return max_window
        if not nums: return 0
        left = 0
        right = 0
        zeros = 0
        count = 0
        while right<len(nums):
            if nums[right] == 0:
                zeros+=1
            while zeros>k:
                if nums[left] == 0:
                    zeros-=1
                left+=1
            count = max(count,right-left+1)
            right+=1
        return count
