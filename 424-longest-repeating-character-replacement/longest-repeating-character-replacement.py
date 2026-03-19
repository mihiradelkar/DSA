class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_freq = 0
        freq = {}
        # right = 0
        # res = 0
        # while right<len(s):
        #     freq[s[right]]= freq.get(s[right],0)+1 
        #     max_freq = max(max_freq,freq[s[right]])
        #     while (right-left+1)-max_freq > k:
        #         freq[s[left]]-=1
        #         left+=1
        #     res = max(res,right-left+1)
        #     right+=1
        # return res
        
        replace = 0
        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right],0)+1
            if freq[s[right]]>max_freq:
                max_freq = freq[s[right]]
            elif replace<k:
                replace+=1
            else:
                freq[s[left]]-=1
                left+=1
        return max_freq+replace