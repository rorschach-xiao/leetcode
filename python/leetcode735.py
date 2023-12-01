from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            explode = False
            while len(stack) > 0 and stack[-1] > 0 and asteroid < 0 and not explode:
                if abs(stack[-1]) < abs(asteroid):
                    stack.pop()
                elif abs(stack[-1]) == abs(asteroid):
                    stack.pop()
                    explode = True
                else:
                    explode = True
            if not explode:
                stack.append(asteroid)

        return stack