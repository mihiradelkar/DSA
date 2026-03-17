class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # Questions:
        #  return any peak not the highest
        #  what if we just have one element?
        #  
        # Approach: 
        # log n is only possible with birnay search
        # shrink the window until mid > left and right
        # 
        # 1,2,1,3,5,6,4
        # l     m     r
        #       l m   r
        #         l m r
        # 1,2,3,1
        # l m   r
        #   l m r
        #   l r
        #   lm r
        #     lr
        
        left = 0
        right = len(nums)-1
        while left < right:
            mid = (left+right)//2
            # only check in next one is greater and do l=mid+1 else just r=mid 
            # when calulating mid for an odd number it will floor to smaller value which will be left 
            # and loop will break when l=r we can return l and the mid point
            if nums[mid]<nums[mid+1]:
                left = mid+1
            else:
                right = mid
        return left