class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        new_mass = mass
        for a in asteroids:
            # print(a,new_mass)
            if new_mass >= a:
                new_mass+=a
            else:
                return False
        return True
        