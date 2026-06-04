class Solution:
    def totalWaviness(self, start: int, end: int) -> int:
        if end < 100:
            return 0
        res = 0
        for num in range(start,end+1):
            n = str(num)
            waviness = 0
            for i in range(1,len(n)-1):
                if int(n[i-1]) > int(n[i]) and int(n[i+1]) > int(n[i]):
                    waviness += 1
                if int(n[i-1]) < int(n[i]) and int(n[i+1]) < int(n[i]):
                    waviness += 1
            res += waviness
        return res