class Solution:
    def calculate(self, s: str) -> int:
        # 3+3+2*2
# questions:
# will the string be empty? yes return 0
# what functions will it support? +-*/
# will it have while spaces? yes skip them
# output in int

# edge cases:
# "" return 0
# support +-*/
# " 3 + 2 " = 5
# answer in range [-231, 231 - 1]

# approach
# right to left select 2 numbers and operate (brute force)
# Parse into tokens, eval two passes (first * and /, then + and -) 
# — O(n) time, O(n) space but complex to implement cleanly.

# find a digt hold it in res and sum later if */ do now
# Data Structure: Stack of pending values
# Algorithm: Parse number → on operator (or end), decide action based on previous operator

        # res = []
        res = 0
        prev = 0
        num = 0
        op = "+"
        for ch in s + "+":
            if ch.isdigit():
                # num = num *10 + int(ch)
                num = num *10 + (ord(ch) - ord("0"))
            elif ch in "+-*/":
                if op == "+":
                    # res.append(num)
                    res += prev
                    prev = num
                elif op == "-":
                    # res.append(-num)
                    res += prev
                    prev = -num
                elif op == "*":
                    # res.append(res.pop()*num)
                    prev *= num
                elif op == "/":
                    # res.append(int(res.pop()/num))
                    prev = int(prev/num)
                num=0
                op=ch
        return res+prev # sum(res)

# Input: s = "3+3+2*2+"
# Output: 10
# res = [3+3,4]
# op = +
# res = 10