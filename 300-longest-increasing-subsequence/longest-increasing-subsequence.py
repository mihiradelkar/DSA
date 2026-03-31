class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # [10,9,2,5,3,7,101,18]
        # [18]
        # [101]
        # [7,18] [7,101]
        # [3,7,101] [3,7,18]
        # [5,7,101] [5,7,18] 
        # [2,5,7,101] [2,5,7,18] [2,3,7,101] [2,3,7,18]
        # [9,101] [9,18]
        # [10,101] [10,18]
        n = len(nums)
        longest = [1] * n
        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                if nums[i]<nums[j]:
                    longest[i] = max(longest[i],1+longest[j])
        return max(longest)