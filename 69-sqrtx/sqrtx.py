class Solution:
    def mySqrt(self, x: int) -> int:
        lo = 1
        hi = x
        res = 0
        while lo<=hi:
            mid = (lo+hi)//2
            curr = mid*mid
            if curr == x:
                return mid
            elif curr < x:
                res = mid
                lo = mid+1
            else:
                hi = mid-1
        return res