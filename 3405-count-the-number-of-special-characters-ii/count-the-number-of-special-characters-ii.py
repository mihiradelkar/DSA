class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        seen_lower = {}
        seen_upper = {}
        count=0
        for i, ch in enumerate(word):
            if ch.islower():
                seen_lower[ch]=i
            else:
                low = ch.lower()
                if low not in seen_upper:
                    seen_upper[low] = i
        # print(seen)
        # for k,v in seen.items():
        #     # print(k,v)
        #     cap = chr(ord(k)-32) 
        #     # print(cap)
        #     if cap in seen and seen[cap]>v:
        #         count+=1
        for low,i in seen_lower.items():
            if low in seen_upper and seen_upper[low]>i:
                count+=1
        return count