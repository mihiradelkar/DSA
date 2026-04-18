class Solution:
    def mirrorDistance(self, n: int) -> int:
        # return abs(n-int(str(n)[::-1]))
        num = n
        rev = 0
        while num > 0:
            rev = (rev*10) + (num%10)
            num = num//10
        return abs(n-rev)