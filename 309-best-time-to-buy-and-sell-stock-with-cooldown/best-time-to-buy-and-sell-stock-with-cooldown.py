class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 0[ 1, 2, 3, 0, 2]
        #   r-h          p
        # rest =  0   0      1      2    2
        # hold = -1  -1|-2  -1|-3  -1|1  1|-1
        # sold = -I   1      2     -1    3

        held = -prices[0]
        sold = float("-inf")
        rest = 0
        for price in prices[1:]:
            p_held,p_sold,p_rest = held,sold,rest
            
            held = max(p_held,p_rest-price)

            sold = p_held+price

            rest = max(p_rest,p_sold)
        
        return max(sold,rest)
        