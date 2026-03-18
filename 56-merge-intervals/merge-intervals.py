class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x:x[0])
        merged = [intervals[0]]
        for start,end in intervals[1:]:
            if start<=merged[-1][1]:
                merged[-1][1] = max(merged[-1][1],end)
            else:
                merged.append([start,end])
        return merged
        

        # Questions:
        #  can the input be empty
        #  Are intervals for sure non-empty
        #  can the ootput be sorted?

        # Approach
        #  Brute force: check every pairs with all other pairs (n^2, n)
        #  Optimmized: sort with start time, compare end with start of next, if smaller modify else append (nlogn, n)

        # res       = [1,3],
        # intervals = [2,6],[8,10],[15,18]

        # intervals.sort(key = lambda i:i[0])         # sort by start so that the overlap are adjacent 
        # res = [intervals[0]]                        # add the first with smallest start interval
        # for start, end in intervals[1:]:            # iterate over all next intervals
        #     if start <= res[-1][1]:                 # Start <= End of Last interval in res. ie there's a overlap
        #         res[-1][1] = max(res[-1][1],end)    # check max interval ending time
        #     else:
        #         res.append([start,end])             # append if no overlap
        # return res