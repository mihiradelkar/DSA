class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        res = 0
        while x!=0:
            # num = (num*10) + (x%10)
            # x //= 10
            x,d = divmod(x,10)
            res = res*10 + d
        if res>(2**31)-1: 
            return 0
        return res if sign == 1 else res*sign
        