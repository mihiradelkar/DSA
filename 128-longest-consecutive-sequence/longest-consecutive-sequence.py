class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        seen = set(nums)
        max_count = 0
        for num in seen:
            if num-1 not in seen:
                count = 1
                while num+1 in seen:
                    count+=1
                    num+=1
                max_count = max(max_count,count)
        return max_count

        