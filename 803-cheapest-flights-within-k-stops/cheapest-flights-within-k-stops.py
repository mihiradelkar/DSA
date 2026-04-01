class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # cities = defaultdict(list)
        # for curr, stop, price in flights:
        #     cities[curr].append((stop,price))
        # print(cities)
        # res = []
        # queue  = [(src,0,0)]
        # visited = set([src])
        # while queue:
        #     cur,stops,total = queue.pop()
        #     if cur == dst:
        #         print(cur,dst)
        #         res.append(total)
        #     print("stops",stops)
        #     if stops>k:
        #         continue
        #     for nxt, price in cities[cur]:
        #         if dst not in visited:
        #             queue.append((nxt,stops+1,total+price))
        #     visited.add(cur)
        # print(res)
        # return min(res)

        # bellman-ford
        prices = [float("inf")] * n
        prices[src] = 0
        
        # cities = defaultdict(list)
        # for c, d, p in flights:
        #     cities[s].append((s,d,p))

        for i in range(k+1):
            pc = prices.copy()
            for s, d, p in flights:
                # print(s,d,p)
                if prices[s] == float("inf"):   # we are starting from the source
                    continue
                if prices[s]+p<pc[d]:           # price to reach cur src + price to dst < cur price to reach dst
                    pc[d] = prices[s]+p         # update the cur price for that dst
            prices = pc
        return prices[dst] if prices[dst] != float("inf") else -1 