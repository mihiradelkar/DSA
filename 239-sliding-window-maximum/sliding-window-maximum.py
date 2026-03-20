class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # [1,3,-1,-3,5,3,6,7]
        # [1][3][3,-1][3,-1,-3]
        queue = deque()
        res = []
        for i in range(len(nums)):
            while queue and queue[0]<i-k+1:
                queue.popleft()
            while queue and nums[queue[-1]]<=nums[i]:
                queue.pop()
            queue.append(i)
            if i+1>=k:
                res.append(nums[queue[0]])
        return res