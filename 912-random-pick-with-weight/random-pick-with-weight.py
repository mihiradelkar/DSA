class Solution:

    # Questions:
    # all weights gerter than 0 ? yes
    # can it be a empty array? no 

    # Approach:
    #  brute force: build expanded array with i appears w[i] times and then picj randomly
    #  time O(1) for pick but O(sum of wiegths) space


    def __init__(self, w: List[int]):
        # [1,3]=>[0,1,1,1]
        # self.index = [i for i, weight in enumerate(w) for _ in range(weight)]  # O(sum(w)) space 
        # [1,3]=>[1,4]
        self.prefix = []
        running = 0
        for weight in w:
            running += weight
            self.prefix.append(running)
        self.total = running
        

    def pickIndex(self) -> int:
        # return self.index[random.randint(0,len(self.index)-1)]        # O(1) time
        target = random.randint(1,self.total)
        # return bisect.bisect_left(self.prefix, target)  # find first prefix >= target
        # same logic as First Bad Version
        left = 0
        right = len(self.prefix)-1
        while left<right:
            mid = (left+right)//2
            if self.prefix[mid] < target:
                left = mid+1
            else:
                right = mid
        return left

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()