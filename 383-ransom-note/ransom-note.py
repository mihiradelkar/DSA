class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count_m = Counter(magazine)

        for ch in ransomNote:
            if ch in count_m and count_m[ch]!=0:
                count_m[ch]-=1
            else:
                return False
        return True
        