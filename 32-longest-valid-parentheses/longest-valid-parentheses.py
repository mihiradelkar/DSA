class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # Stack stores indices; seed with -1 as the left boundary sentinel
        # This handles the case where valid window starts at index 0
        stack = [-1]
        max_len = 0

        for i in range(len(s)):
            if s[i] == '(':
                # Push index of open paren — potential match later
                stack.append(i)
            else:
                # Pop: try to match this ')' with top of stack
                stack.pop()
                if not stack:
                    # No match found — this ')' is unmatched
                    # Push its index as the new left boundary fence
                    stack.append(i)
                else:
                    # Valid span: from (stack[-1] + 1) to i, inclusive
                    max_len = max(max_len, i - stack[-1])

        return max_len