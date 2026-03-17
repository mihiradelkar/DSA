class Solution:
    # step 1: binary search to find target
    # step 2: modify BS to find left target -> # right = mid-1
    # step 3: copy BS for left and make it for right  -> # right = mid-1
    # step 4: merge both BS with flag for switching -> # if leftbias: right = mid-1, else: left = mid+1
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search(nums: List[int], target: int, leftbias:bool) -> int:
        # def searchLeft(nums: List[int], target: int) -> int:
            left = 0
            right = len(nums) -1
            idx = -1
            while left<=right:
                mid = (left + right)//2
                if nums[mid]==target:
                    idx = mid
                    if leftbias:                       # keep seaching even after target is found 
                        right = mid-1                  # shift right to mid for search left
                    else:
                        left = mid+1                   # shift left to mid for search right
                elif nums[mid]<target:
                    left = mid+1
                else:
                    right = mid-1
            return idx
        # def searchRight(nums: List[int], target: int) -> int:
        #     idx = -1
        #     left = 0
        #     right = len(nums) -1
        #     while left<=right:
        #         mid = (left + right)//2
        #         if nums[mid]==target:
        #             idx = mid
        #             left = mid+1                  # shift left to mid for search right
        #         elif nums[mid]<target:
        #             left = mid+1
        #         else:
        #             right = mid-1
        #     return idx
        # return [searchLeft(nums,target), searchRight(nums,target)]
        return [binary_search(nums,target,True), binary_search(nums,target,False)]