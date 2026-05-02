class Solution:
    def rotatedDigits(self, n: int) -> int:
        good = {"2","5","6","9"}
        bad = {"3","4","7"}
        count = 0 

        for i in range(1,n+1):
            num = str(i)
            if any(d in bad for d in num):
                continue
            if any(d in good for d in num):
                count+=1
        return count
        