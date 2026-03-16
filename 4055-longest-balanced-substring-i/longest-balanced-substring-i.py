class Solution:
    def longestBalanced(self, s: str) -> int:
        # Questions:
        #  only lower case letters? yes / make it lower
        #  only one char? return 1
        #  empty string? return 0 
        
        n = len(s)
        res = 0

        # Approach:
        # Brute Force:
        # from left to right count freq of all the chars
        # for left in range(n):
        #     for right in range(left,n+1):
        #         freq = Counter(s[left:right])
        #         if len(set(freq.values())) == 1:

        # Optimal: why count everytime? init counter after left and count as right goes forward 
        # for left in range(n):
        #     freq = Counter()
        #     for right in range(left,n):
        #         freq[s[right]]+=1
        #         if len(set(freq.values())) == 1:
        #             res = max(res, right-left+1)
        
        # Best:
        for left in range(n):
            if n-left <= res:
                return res
            freq = defaultdict(int)
            unique = 0
            max_freq = 0
            for right in range(left,n):
                if freq[s[right]] == 0: unique +=1          # freq[ch]==0: char is seen for the first time: unique+=1  
                freq[s[right]]+=1                           # add freq[ch]
                max_freq = max(max_freq, freq[s[right]])    # claculate max_freq in the substring
                if unique * max_freq == right-left+1:       # if unique*max+freq matches the len of substring
                    res = max(res,right-left+1)             # comapre the prev max values with curr len of sub string
        return res
