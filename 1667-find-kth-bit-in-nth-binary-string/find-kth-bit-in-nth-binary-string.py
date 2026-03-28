class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s_prev = "0"
        if n==1:
            return s_prev
        for i in range(1,n):
            inverted = "".join("1" if bit == "0" else "0" for bit in s_prev)
            s_curr = s_prev + "1" + inverted[::-1]
            s_prev=s_curr
        return s_prev[k-1]
        