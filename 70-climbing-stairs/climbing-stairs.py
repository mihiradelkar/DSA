class Solution:
    def climbStairs(self, n: int) -> int:
        prev = 1
        curr = 2
        if n<2:
            return n
        for i in range(2,n):
            curr,prev = prev+curr, curr
            
        # 0 1 2 3 4 5
        #   1 2 3 5 8
        return curr