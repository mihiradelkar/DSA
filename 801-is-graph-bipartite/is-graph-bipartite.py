class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # adjgraph = [[] for n in range(nodes)]
        # for v in range(nodes):
        #     for u in graph[v]:
        #         adjgraph[v].append(u)
        #         adjgraph[u].append(v)

        nodes = len(graph)
        color = [-1]*nodes

        for n in range(nodes):
            if color[n] != -1:
                continue
            queue = deque([n])
            color[n] = 0
            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if color[neighbor] == -1:
                        color[neighbor] = 1-color[node]
                        queue.append(neighbor)
                    elif color[neighbor] == color[node]:
                        return False
        return True