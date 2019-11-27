class Solution:
    def robot(self, command: str, obstacles, x: int, y: int) -> bool:
        # from itertools import cycle
        # obs = {tuple(obstacle) for obstacle in obstacles}
        # begin = [0, 0]
        # for cmd in cycle(command):
        #     #print(begin)
        #     if tuple(begin) in obs or begin[0] > x or begin[1] > y:
        #         #print(begin)
        #         return False
        #     if begin[0] == x and begin[1] == y:
        #         return True
        #     if cmd == "U":
        #         begin[1] += 1
        #     if cmd == "R":
        #         begin[0] += 1
        from collections import Counter
        from itertools import cycle
        c = Counter(command)

        def helper(i, j):
            right = i
            up = j
            min_c = min(i // c["R"], j // c["U"])
            right -= min_c * c["R"]
            up -= min_c * c["U"]
            #print(right, up)
            for cmd in cycle(command):
                #print(cmd, up, right)
                if up < 0 or right < 0:
                    return False
                if up == 0 and right == 0:
                    return True
                if cmd == "R":
                    right -= 1
                if cmd == "U":
                    up -= 1

        for i, j in obstacles:
            if i <=x and j <=y and helper(i, j):
                #print("df")
                return False
        if helper(x, y): return True
        else:return False


a = Solution()
print(a.robot(command="URR", obstacles=[], x=3, y=2))
print(a.robot(command="URR", obstacles=[[2, 2]], x=3, y=2))
print(a.robot(command="URR", obstacles=[[4, 2]], x=3, y=2))
