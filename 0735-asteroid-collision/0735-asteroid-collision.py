class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for i in asteroids:
            while stack and stack[-1]>0 and i<0:
                diff = i+stack[-1]
                if diff>0:
                    i = 0
                elif diff<0:
                    stack.pop()
                else:
                    i = 0
                    stack.pop()
            
            if i:
                stack.append(i)
        return stack
        