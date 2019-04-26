class Solution:
    def asteroidCollision(self, asteroids):
        if not asteroids:
            return []
        stack = []
        for asteroid in asteroids:
            if asteroid < 0:
                if not stack:
                    stack.append(asteroid)
                else:
                    if stack[-1] < 0:
                        stack.append(asteroid)
                    else:
                        while True:
                            if not stack:
                                stack.append(asteroid)
                                break
                            cur = stack.pop()
                            if cur < 0:
                                stack.append(cur)
                                stack.append(asteroid)
                                break
                            else:
                                if cur == -asteroid:
                                    break
                                elif cur > -asteroid:
                                    stack.append(cur)
                                    break
                                else:
                                    continue
            else:
                stack.append(asteroid)
        return stack


a = Solution()
print(a.asteroidCollision([5, 10, -5]))
print(a.asteroidCollision([8, -8]))
print(a.asteroidCollision([-2, -1, 1, 2]))
print(a.asteroidCollision([]))
print(a.asteroidCollision([-2, -2, -2, -2]))
print(a.asteroidCollision([-2, -2, 1, -2]))
print(a.asteroidCollision([1, -2, -2, -2]))
