class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Monotonic Queue (decresing order) using Deque
        #  [1,3,-1,-3,5,3,6,7]
        #   1  3   -1     -3     5   3   6  7
        #  [1][3][3,-1][3,-1,-3][5][5,3][6][7]  # store idx, small>num pop dq[0] out of window popleft
        # i<k:skip  3      3     5   5   6  7   # res.a(num(dq[0]))
        queue = deque()
        res = []
        for i in range(len(nums)):                      # for all index of nums
            if queue and queue[0]<i-k+1:             # current window size: 1st idx[0] < curr idx - w size +1
                queue.popleft()                         # keep poping from left if ele in dec ord 5 <- [5,4,3] <- 2
            while queue and nums[queue[-1]]<=nums[i]:   # IMPORTANT: check dq[top]<=curr num : no need of keeping small
                queue.pop()                             # keep poping prev is bigger
            queue.append(i)
            if i+1>=k:                                  # window has crossed k start adding ele to res from left
                res.append(nums[queue[0]])
        return res