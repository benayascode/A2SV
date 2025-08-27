# Problem: Asteroid Collision - https://leetcode.com/problems/asteroid-collision/

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        for i in asteroids:
            while st and st[-1]>0 and i < 0:
                if abs(st[-1]) > abs(i):
                    break
                elif abs(st[-1]) == abs(i):
                    st.pop()
                    break
                else:
                    st.pop()
            else:st.append(i)
        return st