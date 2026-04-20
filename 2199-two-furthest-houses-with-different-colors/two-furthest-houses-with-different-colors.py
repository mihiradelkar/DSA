class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)-1
        i = 0
        dist = 0
        while i<n:
            if colors[0]!= colors[n-i] or colors[n]!= colors[i]:
                dist = max(dist, n-i)
            i+=1
        return dist


        