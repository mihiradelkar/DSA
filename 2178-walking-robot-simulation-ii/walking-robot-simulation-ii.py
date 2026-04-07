class Robot:
    
    def __init__(self, width: int, height: int):
        self.w = width
        self.h = height
        self.P = 2 * (width-1) + 2 * (height-1)
        self.total = 0

    def step(self, num: int) -> None:
        self.total += num

    def _decode(self):
        w, h, P = self.w, self.h, self.P
        p = self.total % P 
        print(p)
        if p == 0:
            if self.total  == 0:
                return [0,0] , "East"
            return [0,0] , "South"

        if p <= w-1:
            return [p,0], "East"

        if p <= w+h-2:
            return [w-1,p-(w-1)], "North"

        if p<= 2*w+h-3:
            return [2*w+h-3-p,h-1], "West"
        
        return [0,P-p], "South"

    def getPos(self) -> List[int]:
        pos, _ = self._decode()
        return pos

    def getDir(self) -> str:
        _, d = self._decode()
        return d
            
    # def __init__(self, width: int, height: int):
    #     self.cur_loc = (0,0)
    #     self.m = width-1
    #     self.n = height-1
    #     self.heading = 0
    #     self.headings = ["East","North", "West","South"]

    #     self.move = [(1,0), (0,1), (-1,0), (0,-1)] 

    # def step(self, num: int) -> None:
    #     # print(num)
    #     for i in range(num):
    #         dx,dy = self.move[self.heading]
    #         x,y = self.cur_loc
    #         nx,ny = x+dx,y+dy
    #         # print(nx,ny)
    #         if nx>self.m or ny>self.n or nx<0 or ny<0:
    #             self.heading = (self.heading +1)%4
    #             dx,dy = self.move[self.heading]
    #             x,y = self.cur_loc
    #             nx,ny = x+dx,y+dy
    #         self.cur_loc = (nx,ny)

    # def getPos(self) -> List[int]:
    #     return self.cur_loc

    # def getDir(self) -> str:
    #     return self.headings[self.heading]
        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()