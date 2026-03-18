class Solution:
    def trap(self, height: List[int]) -> int:
        maxleft=maxright=0
        left=0
        right=len(height)-1
        water = 0
        while left<right:
            if height[left]<height[right]:
                if height[left]>maxleft:
                    maxleft=height[left]
                else:
                    water+=maxleft-height[left]
                left+=1
            else:
                if height[right]>maxright:
                    maxright=height[right]
                else:
                    water+=maxright-height[right]
                right-=1
        return water