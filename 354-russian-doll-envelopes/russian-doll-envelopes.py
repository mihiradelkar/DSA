class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # envelopes.sort()
        # # [[2, 3], [5, 4], [6, 5], [6, 6], [7,6]]
        # envelope = [envelopes[0]]
        # for w,h in envelopes[1:]:
        #     # print(w,h)
        #     sw = envelope[-1][0]
        #     sh = envelope[-1][1]
        #     if sw<w and sh<h:
        #         envelope.append([w,h])
        # return len(envelope)
        
        # Brute Force
        # n = len(envelopes)
        # dp = [1]*n
        # envelopes.sort()
        # # print(envelopes)
        # for i in range(n): 
        #     for j in range(i):
        #         if envelopes[j][0]<envelopes[i][0] and envelopes[j][1]<envelopes[i][1]:
        #             dp[i] = max(dp[i],dp[j]+1)
        # # print(dp)
        # return max(dp)

        # [[13, 11], [14, 17], [15, 8], [16, 1], [18, 13], [18, 19]]
        # [[13, 11], [14, 17], [15, 8], [16, 1], [18, 19], [18, 13]]
        # [[13, 11]] t=[11]
        # [[13, 11], [14, 17]] t=[11,17]
        # [[13, 11], [14, 17], [15, 8]] t=[8,17]
        # [[13, 11], [14, 17], [15, 8], [16, 1]] t=[1,17]
        # [[13, 11], [14, 17], [15, 8], [16, 1], [18, 19]] t=[1,17,19]
        # [[13, 11], [14, 17], [15, 8], [16, 1], [18, 19], [18, 13]]  t=[1,13,19]
        # t=[1,13,19] 
        #         ^   new position because all the envelopes before this have a smaller width


        envelopes.sort(key=lambda x:(x[0],-x[1]))
        # Core: a envelopes with greater height is after a smaller height only beacause the width is smaller
        tails = [] # tails is NOT the actual LIS — it's a bookkeeping structure
        for w,h in envelopes:
            pos = bisect_left(tails,h)
            if pos == len(tails):
                tails.append(h)
            else:
                tails[pos] = h
            # print(tails)
        return len(tails)

