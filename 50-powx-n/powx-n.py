class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Questions:
        # so we cant use x**n?
        # can the exponent be negative?
        # can base be negative?

        # Approach:
        # 1: return x**n  # direct in python
        # 2: keep multipling x for n times O(n) : 
        # 3: double x and n//2 O(log n)
        
        # Handle negative exponent: x^(-n) = 1 / x^n

        res = 1
        # if power is negative
        if n<0:
            x = 1/x # flip base
            n = -n  # + power  
        
        # for _ in range(n):
        #     res*=x

        while n>0:
            if n%2==1: # handle odd with end number to be negative and final result in res
                res *= x                
            x*=x            # keep doubling x 
            n = n//2        # half n every time  O(log n)
        return res