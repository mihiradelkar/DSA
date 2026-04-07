class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u,v,w in times:
            graph[u].append((v,w))

        heap = [(0,k)]
        times = {}
        max_t = 0
        while heap:
            # pop neareast node in the heap
            time, node = heapq.heappop(heap)
            if node in times: #alreadt reached means time will always be less
                continue
            times[node] = time
            # max_t = time
            # add all the adjecnt nodes
            for new_node,new_time in graph[node]:
                if new_node not in times: # push the neighbor if not visited
                    heapq.heappush(heap,(new_time+time,new_node))
        # all node not covered time not noted return -1
        if len(times)<n:
            return -1
        # max time taken to reach end
        # return max_t
        return max(times.values())
