class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        seen = set(word)
        count = 0
        # for ch in seen:
        #     if chr(ord(ch)-32) in seen:
        #         count+=1

        for ch in "abcdefghijklmnopqrstuvwxyz":
            if ch in seen and ch.upper() in seen:
                count+=1
        return count

        