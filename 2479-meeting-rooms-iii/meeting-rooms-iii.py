class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()                                             # IMPORTANT
        available = [i for i in range(n)]                   # sorted room no need to heapify
        used = []  #(end,room)
        count = [0] * n 
        for start, end in meetings:
            # finish all meeting with end less than cur start
            while used and start>=used[0][0]:
                _,room = heapq.heappop(used)
                heapq.heappush(available,room)
            # if meeting are not available
            if not available:
                low_end,room = heapq.heappop(used)
                end = low_end+(end-start)
                heapq.heappush(available,room)
            # if meeeting rooms are available
            room = heapq.heappop(available)
            heapq.heappush(used,(end,room))
            count[room] +=1

        # print(count)
        return count.index(max(count))