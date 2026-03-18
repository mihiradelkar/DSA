class MedianFinder:

    def __init__(self):
        # self.nums = []
        self.lower = []
        self.upper = []
        

    def addNum(self, num: int) -> None:
        # self.nums.append(num)
        heapq.heappush(self.lower,-num)

        if self.upper and (-self.lower[0]>self.upper[0]):
            heapq.heappush(self.upper,-heapq.heappop(self.lower))

        if len(self.lower)<len(self.upper):
            heapq.heappush(self.lower,-heapq.heappop(self.upper))
        elif len(self.lower)>len(self.upper)+1:
            heapq.heappush(self.upper,-heapq.heappop(self.lower))

    def findMedian(self) -> float:
        # self.nums.sort()
        # n = len(self.nums)
        # if n%2 == 1:
        #     return float(self.nums[n//2])
        # return (self.nums[(n//2)-1] + self.nums[n//2])/2.0
        if len(self.lower)>len(self.upper):
            return float(-self.lower[0])
        return (-self.lower[0] + self.upper[0])/2.0



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()