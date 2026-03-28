class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        # s_prev = "0"
        # if n==1:
        #     return s_prev
        # for i in range(1,n):
        #     inverted = "".join("1" if bit == "0" else "0" for bit in s_prev)
        #     s_prev = s_prev + "1" + inverted[::-1]
        # return s_prev[k-1]

        if n == 1:
            return "0"
        # 1 << 1  =  10      (binary) = 2
        # 1 << 2  =  100     (binary) = 4
        # 1 << n  =  2^n
        length = (1<<n)-1
        # left and right partition seperated by 1
        mid = (length//2)+1
        #  if k is mid then always "1"
        if k == mid:
            return "1"
        #  k on left side find kth bit on left
        elif k<mid:
            return self.findKthBit(n-1,k)
        #  k on right side find total - k +1 bit on left
        # findKthBit(3,5): length=7, mid=4, k>mid → mirrored=7-5+1=3
        else:
            mirrored = length-k+1
            bit = self.findKthBit(n-1,mirrored)
            return "1" if bit == "0" else "0" 

        