class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        airport = defaultdict(list)
        # print(sorted(tickets, reverse=True))
        # for src, dst in sorted(tickets, reverse=True):
        # Adj list
        for src, dst in tickets:
            airport[src].append(dst)
        # sort dst list for smaller lexical order 
        for src in airport.keys():
            airport[src].sort(reverse=True)
        # print(airport)
        #  post order dfs from JFK
        res = []
        def dfs(src):
            while airport[src]:
                dst = airport[src].pop()
                dfs(dst)
            res.append(src)
        dfs("JFK")
        return res[::-1]
        