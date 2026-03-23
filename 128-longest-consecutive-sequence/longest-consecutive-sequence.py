class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        seen = set(nums)
        max_count = 0
        for num in seen:
            if num-1 not in seen:
                count = 1
                cur = num
                while cur+1 in seen:
                    count+=1
                    cur+=1
                max_count = max(max_count,count)
        return max_count

        