class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        airport = defaultdict(list)
        # print(sorted(tickets, reverse=True))
        for src, dst in sorted(tickets, reverse=True):
            airport[src].append(dst)
        res = []
        def dfs(src):
            while airport[src]:
                dst = airport[src].pop()
                dfs(dst)
            res.append(src)
        dfs("JFK")
        return res[::-1]
        