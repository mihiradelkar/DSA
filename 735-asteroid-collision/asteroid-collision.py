class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for curr in asteroids:
            alive = True
            while alive and curr<0 and stack and stack[-1]>0:
                top = stack[-1]
                if top<abs(curr):
                    stack.pop()
                elif top==abs(curr):
                    stack.pop()
                    alive = False
                else:
                    alive = False
            if alive:
                stack.append(curr)
        return stack 
