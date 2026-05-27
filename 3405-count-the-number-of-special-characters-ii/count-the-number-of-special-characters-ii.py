class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower = {}
        upper = {}
        for i, ch in enumerate(word):
            if ch.islower():
                lower[ch]=i
            else:
                if ch not in upper:
                    upper[ch] = i
        count=0
        for c,i in lower.items():
            cap = c.upper()
            if cap in upper and upper[cap]>i:
                count+=1
        return count

        # print(seen)
        # for k,v in seen.items():
        #     # print(k,v)
        #     cap = chr(ord(k)-32) 
        #     # print(cap)
        #     if cap in seen and seen[cap]>v:
        #         count+=1