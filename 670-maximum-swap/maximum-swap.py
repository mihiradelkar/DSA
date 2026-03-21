class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))                                 # convert num->str->list
        last = {int(d):i for i, d in enumerate(digits)}         # index of last seen digit

        for i, d in enumerate(digits):                          # enumerate over digit to replace
            for bigger in range(9,int(d),-1):                   # 9 to cur digit - largest possible swap
                if last.get(bigger,-1)>i:                       # if found a bigger num on right for swap
                    j = last[bigger]
                    digits[i],digits[j] = digits[j],digits[i]
                    return int("".join(digits))
        return num