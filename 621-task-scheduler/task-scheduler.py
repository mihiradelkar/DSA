class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # ["A","A","A","B","B","C"], n = 2
        # {A:3, B:2, C:1}
        # time = 0 heap = [-3,-2,-1] queue = []
        # time = 1 heap = [-2,-1] queue = [(-2,3)]
        # time = 2 heap = [-1] queue = [(-2,3),(-1,4)]
        # time = 3 heap = [-2] queue = [(-1,4)]
        # time = 4 heap = [-1] queue = [(-1,6)]
        # time = 5 heap = [] queue = [(-1,6)]
        # time = 6 heap = [-1] queue = []
        # time = 7 heap = [] queue = []



        count = Counter(tasks)
        heap = [-cnt for cnt in count.values()]
        heapq.heapify(heap)
        queue = deque()
        time = 0
        while heap or queue:
            time+=1
            if heap:
                cnt = 1+heapq.heappop(heap)
                if cnt:
                    queue.append((cnt,time+n))
            if queue and queue[0][1]==time:
                heapq.heappush(heap,queue.popleft()[0])
        return time
        


        # # [SETUP] — count frequency of each task; only 26 possible so O(1) space
        # count = Counter(tasks)
        # # [KEY VALUES] — the most frequent task controls the frame skeleton
        # max_count = max(count.values())
        # # count tasks tied for max_freq — they all appear in the last partial frame
        # total_max_count = sum(1 for cnt in count.values() if max_count == cnt)
        # # [FORMULA] — (max_freq-1) full frames of (n+1) slots, plus last partial frame
        # # [RETURN] — if tasks are dense enough, no idles needed; just run all tasks
        # return max(len(tasks),(max_count-1)*(n+1)+total_max_count)