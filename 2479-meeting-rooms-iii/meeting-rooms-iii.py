class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        available = [i for i in range(n)]
        used = [] #(end,room)
        count = [0] * n
        for start, end in meetings:
            # finish all meeting with end less than cur start
            while used and start>=used[0][0]:
                _,room = heapq.heappop(used)
                heapq.heappush(available,room)
            # if meeeting rooms are available
            if available:
                room = heapq.heappop(available)
                heapq.heappush(used,(end,room))
                count[room] +=1
            # if meeting are not available
            else:
                last_end,room = heapq.heappop(used)
                heapq.heappush(used,(last_end+(end-start),room))
                count[room] +=1

        # print(count)
        return count.index(max(count))