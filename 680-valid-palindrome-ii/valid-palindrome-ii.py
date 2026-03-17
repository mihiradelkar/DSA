class Solution:
    def validPalindrome(self, s: str) -> bool:
        # question 
        # lower case only ?
        # will there be space?
        # empty string?
        # only one deletion allowed?
        
        # approach 
        # brute force: try removing each character and check if palindrome n^2
        # optimized: two poniter => walk inward on mismatch try skip left or right and check if palindrome

        # complexity O(n) space o(1)
        
        def isPalindrome(left,right):
            while left<right:
                if s[left]!=s[right]:
                    return False
                left+=1
                right-=1
            return True
        left = 0
        right = len(s)-1
        while left<right:
            if s[left]!=s[right]:
                return (isPalindrome(left,right-1) or isPalindrome(left+1,right))
            left+=1
            right-=1
        return True

        # Follow up : 125,1216 variant