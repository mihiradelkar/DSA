class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        clean = set(word)
        count = 0
        for ch in clean:
            if chr(ord(ch)-32) in clean:
                count+=1
        return count

        