class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0]*n
        stack = []

        for i in range(n-1, -1, -1):
            g_min = g_max = nums[i]
            right = i
            while stack and stack[-1][0] < g_max:
                top_min,top_max,top_right = stack.pop()
                g_min = min(g_min,top_min)
                g_max = max(g_max,top_max)
                right = top_right
            stack.append((g_min,g_max,right))

        left = 0
        for g_min,g_max,right in reversed(stack):
            for i in range(left,right+1):
                res[i]= g_max
            left=right+1
        return res

        